#!/bin/bash
# Morning Automation Script
# Runs at 6:00 AM PST daily

echo "=== MAVERICK MORNING ROUTINE ==="
echo "Started: $(date)"

# 1. Research Agent - Check overnight trends
echo "[1/5] Running Research Agent..."
# Triggers sessions_spawn for research agent

# 2. Generate first script
echo "[2/5] Spawning Script Agent for priority topic..."
# Triggers script agent with top trending topic

# 3. Generate second script  
echo "[3/5] Spawning Script Agent for second topic..."

# 4. Generate third script
echo "[4/5] Spawning Script Agent for third topic..."

# 5. Deliver summary
echo "[5/5] Sending morning briefing to David..."

echo "=== ROUTINE COMPLETE ==="
echo "Finished: $(date)"
