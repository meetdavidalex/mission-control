# Vibes Academy Script: From Vibe Coded App to Real Product: Deployment & Scaling Guide

**Target Channel:** Vibes Academy  
**Target Length:** 10-14 minutes spoken  
**Tone:** Practical, empowering, step-by-step — like a tech lead showing you the path from prototype to production

---

## SEO Titles

1. **From Vibe Coded App to Real Product: The Complete Deployment Guide**
2. **How to Deploy Your AI-Built App: GitHub, Vercel & Custom Domain Tutorial**
3. **Vibe Coding Part 3: Taking Your App Live (The Right Way)**
4. **Stop Leaving Your Apps on Localhost: Deploy Like a Pro in 2025**
5. **The Missing Step in Vibe Coding: How to Actually Ship Your App**

---

## Hooks

### Hook 1: The Deployment Gap
*Context Lean:* "You've built your first app with Lovable or Bolt. It looks great, it works on your screen, and you're proud of what the AI helped you create."  
*Scroll Stop:* "But here's the problem: it's still trapped on their servers, and you have no idea how to actually put it somewhere you control."  
*Contrarian Snapback:* "Today I'm going to show you exactly how to take any vibe-coded app, move it to your own GitHub, deploy it to production, and connect a real domain — even if you've never done any of this before."

### Hook 2: The Ownership Reality
*Context Lean:* "Vibe coding is amazing for getting something built fast. But most people stop there — they have a working app they don't actually own, sitting on someone else's platform."  
*Scroll Stop:* "And when that platform changes pricing, changes features, or has downtime, you're stuck."  
*Contrarian Snapback:* "The difference between someone who 'plays with AI' and someone who ships real products is this deployment step. Let me show you how to cross that gap."

### Hook 3: The Portfolio Problem
*Context Lean:* "If you're learning vibe coding to build a portfolio, get freelance clients, or start a side project, listen up."  
*Scroll Stop:* "Nobody hires developers who show them apps running on Lovable's preview URLs. You need your own domain, your own deployment, your own GitHub repo."  
*Contrarian Snapback:* "This video is the bridge between 'I built something cool' and 'I'm a developer who ships.' Let's build that bridge together."

---

## Full Script

### SECTION 1: INTRO (60 seconds)

**[Opening — direct to camera]**

Welcome back to Vibes Academy. If you've been following along, you now know how to build apps with AI tools, and you know the mistakes to avoid along the way. But there's one more critical step we haven't covered: how to actually ship what you've built.

See, here's the thing about vibe coding — it's incredibly powerful for getting from zero to something that works. But that "something" usually lives on someone else's servers. Lovable's servers. Replit's servers. Bolt's preview environment.

If you want to show your app to potential employers, share it with users, or just actually own what you've built, you need to get it onto your own infrastructure. And that's what today's video is about.

I'm going to walk you through the complete deployment pipeline: exporting your code to GitHub, deploying to a production host, connecting a custom domain, and setting up the basics that separate hobby projects from real products.

This is the step that turns a vibe-coded experiment into something you can put on your resume. Let's get into it.

---

### SECTION 2: WHY DEPLOYMENT MATTERS (90 seconds)

**[Screen recording — showing different hosting environments]**

Before we dive into the how, let's talk about the why. Because I know what some of you are thinking: "The preview link works fine. Why complicate things?"

Three reasons.

**First: ownership.** When your app only exists on Lovable's platform, you don't really own it. You can't easily move it elsewhere. If Lovable changes their pricing or shuts down a feature you rely on, you're stuck rebuilding.

**Second: credibility.** If you're building a portfolio to get hired or land freelance clients, showing someone a Lovable preview URL says "I can use AI tools." Showing them a custom domain with your name on it says "I understand the full development lifecycle." That's a huge difference.

**Third: features.** Preview environments are limited. You can't set up custom domains, configure SSL properly, add analytics, or do a dozen other things that real apps need. Production hosting unlocks all of that.

**[Back to camera]**

The good news? This isn't as hard as it used to be. What once required a DevOps engineer and a week of configuration now takes about thirty minutes. The tools have gotten that good.

---

### SECTION 3: THE DEPLOYMENT PIPELINE OVERVIEW (60 seconds)

**[Screen recording — diagram showing the pipeline]**

Here's what we're going to do, step by step:

1. **Export your code to GitHub** — This gives you version control and a portable copy of your app
2. **Set up a production database** — Moving from the AI tool's managed DB to one you control
3. **Deploy to Vercel** — This hosts your frontend and gives you a production URL
4. **Connect a custom domain** — So your app lives at something like myapp.com instead of a random Vercel URL
5. **Configure environment variables** — Making sure your production app can talk to your production database

**[Back to camera]**

Don't worry if some of those terms sound unfamiliar. I'm going to explain each one as we go, and by the end of this video, you'll have done all of them.

---

### SECTION 4: STEP 1 — EXPORTING TO GITHUB (3 minutes)

**[Screen recording — Lovable interface, GitHub integration]**

Let's start with getting your code out of the AI tool and into a place you control. If you built your app with Lovable, this is actually built-in.

**[Screen recording — showing the GitHub sync process]**

In Lovable, click the GitHub icon in the top right. You'll need to connect your GitHub account if you haven't already. Once connected, Lovable will create a repository for your project and push every change as a commit.

This is huge. Every time you make a change in Lovable, it shows up as a commit in GitHub. You can see exactly what changed, roll back to previous versions, and most importantly — you now have your code in a standard format that any developer or hosting platform can work with.

**[Screen recording — showing the GitHub repository]**

Let's look at what we got. Your repository contains:
- All your React/TypeScript code
- Configuration files
- A README (which you should update)
- Package.json showing your dependencies

This is a real, standard codebase now. You could open this in VS Code, hand it to another developer, or deploy it anywhere that supports React apps.

**[Screen recording — showing Bolt export process]**

If you built with Bolt instead of Lovable, the process is similar but manual. In Bolt, go to the menu and select "Download code." This gives you a zip file with everything. Extract it, then go to GitHub and create a new repository. Upload the files, and you're in the same place.

**[Back to camera]**

The key point: your code is now portable. You're not locked into any single platform anymore. This is the foundation everything else builds on.

---

### SECTION 5: STEP 2 — SETTING UP A PRODUCTION DATABASE (3 minutes)

**[Screen recording — Supabase dashboard]**

Now let's talk about your database. When you built your app with an AI tool, it probably set up a database for you automatically. But that database lives on their infrastructure, and you can't easily access it from outside their platform.

For a production app, you need a database you control. My recommendation for beginners is Supabase. It's free to start, it's built on PostgreSQL which is industry standard, and it has a generous free tier that'll handle plenty of real users.

**[Screen recording — creating a new Supabase project]**

Go to supabase.com and create an account if you don't have one. Click "New Project" and give it a name. Choose the region closest to your users — if you're in the US, use a US region. If you're targeting a global audience, US East is usually a safe default.

**[Screen recording — showing the database connection info]**

Once your project is created, Supabase will show you connection details. You need two things: the database URL and the anon key. These are like a username/password for your app to talk to the database.

**[Screen recording — showing how to export data from Lovable]**

Now, if you have data in your Lovable database that you want to keep, you'll need to export it. This is the trickiest part. In Lovable, go to your Supabase dashboard (they use Supabase under the hood), find the table you want to export, and use the export function to get a CSV.

Then in your new Supabase project, create a table with the same structure and import that CSV. It's a bit manual, but you only have to do it once.

**[Screen recording — showing the SQL editor in Supabase]**

Actually, there's an easier way if you're comfortable with SQL. Supabase has an "SQL Editor" where you can run commands. You can export your entire database schema from Lovable and run it here to recreate all your tables at once.

**[Back to camera]**

I know this sounds technical, but here's the thing: you're learning real database skills right now. This isn't vibe coding anymore — this is actual backend development. And it's way more accessible than it used to be.

---

### SECTION 6: STEP 3 — DEPLOYING TO VERCEL (3 minutes)

**[Screen recording — Vercel dashboard]**

Now for the fun part: getting your app live on the internet. We're going to use Vercel, which is specifically designed for React apps like the ones these AI tools generate.

**[Screen recording — connecting GitHub to Vercel]**

Go to vercel.com and sign up. You can use your GitHub account to log in — this makes everything easier. Once you're in, click "Add New Project" and select "Import Git Repository."

Vercel will show you all your GitHub repos. Find the one with your app and click "Import."

**[Screen recording — project configuration]**

Now Vercel asks for some configuration. The defaults are usually fine for React apps, but there's one critical thing we need to add: environment variables.

Remember those database credentials from Supabase? This is where they go. Click "Environment Variables" and add two:

1. `VITE_SUPABASE_URL` — paste your Supabase project URL here
2. `VITE_SUPABASE_ANON_KEY` — paste your anon key here

These names might vary depending on how your app was built. Check your code for what environment variable names it expects — they're usually at the top of files that connect to the database.

**[Screen recording — clicking deploy]**

Click "Deploy" and watch the magic happen. Vercel will:
- Pull your code from GitHub
- Install all your dependencies
- Build your app
- Deploy it to their global network

This usually takes 1-2 minutes. When it's done, you'll get a URL like `myapp-abc123.vercel.app`. Click it — your app is now live on the internet.

**[Screen recording — showing the live app]**

But we're not done yet. That URL works, but it's not yours. Let's fix that.

---

### SECTION 7: STEP 4 — CONNECTING A CUSTOM DOMAIN (3 minutes)

**[Screen recording — domain registrar, Vercel domain settings]**

Having your app on a random Vercel URL is fine for testing, but for anything serious, you want your own domain. Something like `myapp.com` or `davidstaskmanager.com`.

If you don't have a domain yet, go to a registrar like Namecheap, Cloudflare, or Google Domains and buy one. They're usually $10-15 per year. For this demo, I'm going to assume you have one.

**[Screen recording — adding domain in Vercel]**

In Vercel, go to your project settings and find "Domains." Click "Add" and type your domain name.

Vercel will give you instructions for configuring your DNS. This is the technical part that scares people, but it's actually simple.

**[Screen recording — DNS configuration]**

You need to add two records in your domain registrar's DNS settings:

1. An A record pointing to Vercel's IP address (they'll give you the exact IP)
2. A CNAME record for the www version pointing to `cname.vercel-dns.com`

Every registrar has a slightly different interface, but they all have a "DNS" or "DNS Management" section. Add those two records, save, and wait.

**[Back to camera]**

DNS changes take time to propagate — anywhere from a few minutes to 48 hours. Usually it's under an hour. You can check if it's working by running `nslookup yourdomain.com` in a terminal or just trying to visit it.

**[Screen recording — showing the custom domain working]**

Once it propagates, visiting your domain will show your app. And Vercel automatically handles SSL certificates, so your site will have that secure https:// lock icon. They renew automatically forever.

**[Back to camera]**

Think about what just happened. You now have:
- Your code on GitHub
- Your database on Supabase
- Your frontend deployed on Vercel
- Your own custom domain with SSL

That's a complete production stack. That's what real companies use. And you just set it up yourself.

---

### SECTION 8: STEP 5 — TESTING & MONITORING (2 minutes)

**[Screen recording — testing the deployed app]**

Now that you're deployed, let's make sure everything actually works. Test all your app's features:
- Can you sign up?
- Can you create items?
- Do they save to the database?
- Do they persist after refresh?

**[Screen recording — showing Vercel analytics]**

Vercel has built-in analytics you can enable. This shows you how many people visit your site, where they're from, what devices they use. It's not as detailed as Google Analytics, but it's easier to set up and respects user privacy better.

**[Screen recording — showing Supabase logs]**

Supabase also has monitoring. You can see your database usage, slow queries, error logs. If something breaks, this is where you'll find clues.

**[Back to camera]**

Here's a pro tip: set up a simple uptime monitor. There are free services like UptimeRobot that will check your site every few minutes and email you if it goes down. For a production app, you want to know about problems before your users do.

---

### SECTION 9: COMMON DEPLOYMENT ISSUES (3 minutes)

**[Screen recording — showing error messages]**

Let me save you some headaches by covering the most common problems people hit when deploying.

**Issue 1: Environment variables not set**

If your app works locally or in preview but fails in production, 90% of the time it's missing environment variables. Double-check that you added them in Vercel's settings and that the names match exactly what your code expects.

**Issue 2: Database connection errors**

If your app loads but can't save data, check your Supabase connection. Make sure you copied the URL and key correctly. Make sure your database tables exist. Check Supabase's logs for connection errors.

**Issue 3: Build failures**

Sometimes Vercel fails to build your app. Click on the deployment and read the error logs. Common causes: missing dependencies, syntax errors, or trying to use browser-only APIs in server-side code.

**Issue 4: CORS errors**

If your frontend and backend are on different domains, you might get CORS errors. Supabase handles this automatically, but if you're using a different backend, you might need to configure CORS headers.

**[Screen recording — showing how to read error logs]**

The key skill here is reading error logs. They're intimidating at first, but they usually tell you exactly what's wrong. Look for the red text, read the message, Google it if you don't understand. This is how developers solve problems.

---

### SECTION 10: THE MINDSET SHIFT (90 seconds)

**[Back to camera — more personal tone]**

I want to pause here and talk about something important. Because what you just did — even if you haven't done it yet, even if you're just watching — represents a mindset shift.

Vibe coding is about speed. It's about getting from idea to working prototype as fast as possible. And that's valuable. But deployment is about ownership. It's about taking responsibility for your code, understanding how it fits into the larger system, and making it sustainable.

When you deploy an app, you're not just clicking buttons. You're learning:
- How version control works
- How databases are hosted and accessed
- How web hosting works
- How domains and DNS work
- How to troubleshoot when things break

These are real developer skills. The kind that get you hired. The kind that let you build things that last.

**[Screen recording — showing a portfolio with multiple deployed projects]**

I know this video was more technical than the previous ones. That's intentional. The first video got you building. The second kept you from common mistakes. This one is about leveling up — about becoming someone who can actually ship.

---

### SECTION 11: RECAP & NEXT STEPS (60 seconds)

**[Direct to camera]**

Let's recap what we covered:

1. **Export to GitHub** — Get your code out of the AI tool and into version control
2. **Set up Supabase** — Create a production database you control
3. **Deploy to Vercel** — Host your frontend with automatic builds from GitHub
4. **Connect a domain** — Make your app accessible at your own URL
5. **Test and monitor** — Make sure everything works and set up alerts

This pipeline works for almost any vibe-coded app. The specifics might vary depending on what AI tool you used and what features your app has, but the principles are the same.

**[Back to camera]**

Your homework: take one of the apps you've built and deploy it following these steps. Even if it's just a simple to-do list. Get it on your own domain. Show it to someone. That's the moment you stop "playing with AI" and start being a developer who ships.

---

### SECTION 12: CTA (45 seconds)

**[Direct to camera]**

If you've been following this series, you now have everything you need to go from zero to deployed: how to build with AI, what mistakes to avoid, and how to ship like a pro.

But I'm not done yet. I'm building something for people who want to go deeper — not just one-off tutorials, but a complete system for learning vibe coding from first app to first paying customer. If that sounds like you, check the link in the description for early access.

And if you deploy something using this guide, I want to see it. Drop your domain in the comments — I'll check them out and feature the best ones in a future video.

Thanks for watching. Now go ship something.

---

## Production Notes

### B-Roll Suggestions
- Screen recordings of every step (Lovable, GitHub, Supabase, Vercel)
- Split-screen showing before/after (preview URL vs custom domain)
- Terminal/command line footage for DNS verification
- Dashboard tours of each platform
- Error message close-ups with annotations

### Thumbnail Concept
- Split design: "Localhost" with red X on left, "YourDomain.com" with green check on right
- David pointing at the transition
- Text: "How to Actually Ship"
- Vibes Academy branding

### Related Videos to Link
- Previous Vibes Academy: "Vibe Coding for Beginners" (Part 1)
- Previous Vibes Academy: "7 Vibe Coding Mistakes" (Part 2)
- David Alex channel: Tool comparisons and reviews

### SEO Keywords
vibe coding deployment, lovable deploy to production, vercel tutorial, supabase setup, custom domain setup, github deployment, react app deployment, ai coding production, vibe coding tutorial 2025, deploy app for beginners

### Resources to Link in Description
- GitHub: github.com
- Supabase: supabase.com
- Vercel: vercel.com
- Namecheap: namecheap.com
- UptimeRobot: uptimerobot.com

---

**Word Count:** ~2,800 words  
**Estimated Spoken Length:** 12-14 minutes (expands to ~3,400-3,600 words with natural delivery, pauses, and screen narration)
