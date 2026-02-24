# Multi-Agent System Architecture
# Based on Alex Finn's OpenClaw mastery principles

## Agent Roles

### 1. ORCHESTRATOR (Maverick/Main)
- Receives all requests
- Spawns sub-agents for specific tasks
- Aggregates results
- Delivers final output to user

### 2. RESEARCH AGENT
**Job:** Monitor trends, competitors, opportunities
**Schedule:** Every 2 hours + on-demand
**Outputs:**
- Threads trending report (1K+ engagement posts)
- YouTube trending in niche
- Competitor content analysis
- Brand opportunity alerts

### 3. SCRIPT AGENT  
**Job:** Write full scripts from briefs
**Trigger:** On-demand or scheduled
**Inputs:** Topic, channel, brand/offer, angle
**Outputs:**
- 5 SEO titles
- 3 hooks (3-step formula)
- Full 8-12 minute script
- Talking points
- CTA placement

### 4. HOOK AGENT
**Job:** Generate viral hooks only
**Trigger:** When Script Agent needs options
**Output:** 3 hooks using Context Lean → Scroll Stop → Contrarian Snapback

### 5. REVIEW AGENT
**Job:** Quality control all outputs
**Trigger:** After any agent completes work
**Checks:**
- Voice match (David Alex style)
- Requirements compliance
- Hook quality
- SEO optimization
- Sponsor mention placement

### 6. SOCIAL AGENT
**Job:** Create companion content
**Trigger:** When script approved
**Outputs:**
- 3 Threads posts per video
- LinkedIn post
- Newsletter snippet

## Daily Workflow (Automated)

### 6:00 AM PST - Morning Prep
1. Research Agent checks Threads/YouTube overnight
2. Identifies 3-5 trending topics
3. Prioritizes based on David's content calendar

### 8:00 AM PST - Script Generation
1. Script Agent picks highest priority topic
2. Hook Agent generates 3 hook options
3. Script Agent writes full script
4. Review Agent checks quality
5. Delivers to Notion + notifies David

### 10:00 AM PST - Second Script
1. Repeat for second priority topic
2. Different channel if needed

### 12:00 PM PST - Third Script + Threads Report
1. Third script delivered
2. Full Threads trending report
3. Social Agent drafts companion posts

### 2:00 PM PST - Afternoon Check
1. Research Agent checks for urgent trends
2. Alerts if breaking news/opportunity

### 4:00 PM PST - Evening Prep
1. Preps topics for tomorrow
2. Updates content calendar

## Handoff Protocol

```
Research Agent → Finds topic → Spawns Script Agent
Script Agent → Needs hooks → Spawns Hook Agent
Script Agent → Complete → Spawns Review Agent
Review Agent → Approved → Spawns Social Agent
All Agents → Report to Orchestrator → Deliver to David
```

## Communication

- **Telegram:** Primary interface for David
- **Notion:** Script delivery + archive
- **Dashboard:** Visual status + quick actions
- **Cron:** Triggers scheduled agents

## Success Metrics

- 3 scripts delivered by 10 AM daily
- 100% voice match on all scripts
- 5+ viral Threads identified daily
- < 5 min response time on manual requests
