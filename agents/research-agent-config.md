# Research Agent Configuration

## Data Sources

### Threads Monitoring
- Search terms: "vibe coding", "AI tools", "Claude", "Cursor", "Lovable", "Replit"
- Minimum engagement: 1,000 likes
- Check frequency: Every 2 hours
- Output format: Title, engagement, account, content summary, remake angle

### YouTube Monitoring
- Channels to track: Fireship, Theo, Primeagen, Web Dev Cody
- Keywords: SaaS, AI coding, no-code, startup
- Look for: High view velocity in first 24h

### Competitor Tracking
- Track: Similar content creators in niche
- Monitor: Upload frequency, topics, engagement
- Alert: When they post about trending topic

## Output Template

```markdown
## Threads Trending Report - {{date}}

### Tier 1 (1K+ likes)
1. **{{title}}** - {{engagement}} likes
   - Account: @{{account}}
   - Why trending: {{analysis}}
   - Remake angle: {{angle}}
   - Action: [Remake This] [Save for Later]

### Tier 2 (500-1K likes)
...

### Opportunities
- {{brand}} mentioned in comments (partnership opportunity?)
- {{topic}} gaining momentum (get ahead of trend)
```

## Automation

Cron: `0 */2 * * *` (every 2 hours)
Delivery: Telegram + Dashboard update
