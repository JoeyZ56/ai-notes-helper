# 📝 AI Notes Helper

A smart note-taking app that helps you write, organize, and summarize your notes using AI.

## 💡 Project Goals

- Showcase full-stack web development (Next.js + Python backend)
- Integrate free AI models for text summarization/tagging
- Learn practical AI development while keeping web dev skills sharp

---

## 🧱 Tech Stack

- **Frontend**: Next.js + React + Tailwind
- **Backend**: Python 3.12 + FastAPI
- **AI Integration**: OpenRouter API (free GPT-like models)
- **Database**: Firebase (or Supabase)
- **Hosting**: Vercel (frontend) + Render/Fly.io (backend)

---

## 🚧 Features (Planned)

- [ ] Create, edit, delete markdown notes
- [ ] Organize notes with tags
- [ ] Summarize notes using AI
- [ ] Suggest tags with AI
- [ ] Save notes to user account (auth)
- [ ] Dark mode

---

## 🔄 Workflow

1. **Frontend** (Next.js)

   - Note editor
   - Dashboard
   - AI action buttons (e.g., “Summarize”)

2. **Backend** (FastAPI)

   - Receives note text → sends it to AI API → returns result
   - Handles auth and note storage (if not using Firebase)

3. **AI Layer**
   - Interact with OpenRouter or OpenAI (dev key)
   - Prompt templates to control tone/style of summaries

---

## ✅ Done When...

- The app can summarize and tag notes via AI
- Clean UX with good design and responsiveness
- Secure user data storage and auth
- Deployed and demo-ready
