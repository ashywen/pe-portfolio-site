// Cloudflare Pages Function: same contract as the Flask /api/timeline_post route.
// Requires a D1 database bound to this Pages project with the variable name "DB".

const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const LIMITS = { name: 100, email: 254, content: 2000 };

export async function onRequestGet({ env }) {
  // Emails are stored but never returned publicly.
  const { results } = await env.DB.prepare(
    "SELECT id, name, content, created_at FROM timeline_post ORDER BY created_at DESC LIMIT 100"
  ).all();
  return Response.json({ timeline_posts: results });
}

export async function onRequestPost({ request, env }) {
  let form;
  try {
    form = await request.formData();
  } catch {
    return new Response("Invalid form data", { status: 400 });
  }

  const name = String(form.get("name") ?? "").trim();
  const email = String(form.get("email") ?? "").trim();
  const content = String(form.get("content") ?? "").trim();

  if (!name || name.length > LIMITS.name) return new Response("Invalid name", { status: 400 });
  if (!content || content.length > LIMITS.content) return new Response("Invalid content", { status: 400 });
  if (!EMAIL_RE.test(email) || email.length > LIMITS.email) return new Response("Invalid email", { status: 400 });

  const createdAt = new Date().toISOString();
  const row = await env.DB.prepare(
    "INSERT INTO timeline_post (name, email, content, created_at) VALUES (?, ?, ?, ?) RETURNING id, name, content, created_at"
  )
    .bind(name, email, content, createdAt)
    .first();

  return Response.json(row);
}
