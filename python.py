import pandas as pd

# Load match and athlete data
match_stats = pd.read_csv("C:/Users/Sathvik/Downloads/syracuse_lacrosse_2025_cleaned.csv")
athlete_stats = pd.read_csv("C:/Users/Sathvik/Downloads/syracuse_lacrosse_2025_player_stats.csv")

# Total number of matches
match_count = match_stats.shape[0]

# Calculate wins and losses
wins = match_stats[match_stats["Result"] == "W"].shape[0]
losses = match_stats[match_stats["Result"] == "L"].shape[0]

# Player with most goals
leading_scorer = athlete_stats.sort_values(by="Goals", ascending=False).iloc[0]

# Player with best point average per appearance
athlete_stats["Avg_Points"] = athlete_stats["Points"] / athlete_stats["Games_Played"]
top_avg_point_player = athlete_stats.sort_values(by="Avg_Points", ascending=False).iloc[0]

# Closest margin match
match_stats["Goal_Margin"] = abs(match_stats["SU_Score"] - match_stats["Opponent_Score"])
tightest_match = match_stats.sort_values("Goal_Margin").iloc[0]

# Game with highest team score
highest_scoring_match = match_stats.sort_values("SU_Score", ascending=False).iloc[0]

# Most consistent scorer (goals per game)
athlete_stats["Goal_Rate"] = athlete_stats["Goals"] / athlete_stats["Games_Played"]
consistent_scorer = athlete_stats.sort_values(by="Goal_Rate", ascending=False).iloc[0]

# Assist leader
assist_king = athlete_stats.sort_values(by="Assists", ascending=False).iloc[0]

# Analyze close defeats (within 3-point margin)
match_stats["Score_Diff"] = match_stats["SU_Score"] - match_stats["Opponent_Score"]
close_defeats = match_stats[(match_stats["Result"] == "L") & (match_stats["Score_Diff"] >= -3)]
close_defeat_count = close_defeats.shape[0]

# Match with biggest win margin
top_win = match_stats[match_stats["Result"] == "W"].sort_values(by="Score_Diff", ascending=False).iloc[0]

# Summary Results
print(f"🏟️ Total games played: {match_count}")
print(f"📊 Win/Loss tally: {wins} Wins / {losses} Losses")
print(f"🎯 Leading scorer: {leading_scorer['Player']} with {leading_scorer['Goals']} goals")
print(f"🔥 Highest average points/game: {top_avg_point_player['Player']} ({top_avg_point_player['Avg_Points']:.2f} PPG)")
print(f"⚔️ Tightest match: vs {tightest_match['Opponent']} on {tightest_match['Date']} ({tightest_match['SU_Score']}-{tightest_match['Opponent_Score']})")
print(f"🏆 Top-scoring game: {highest_scoring_match['SU_Score']} goals vs {highest_scoring_match['Opponent']}")
print(f"🎯 Most consistent scorer: {consistent_scorer['Player']} ({consistent_scorer['Goal_Rate']:.2f} goals/match)")
print(f"🅰️ Assist leader: {assist_king['Player']} with {assist_king['Assists']} assists")
print(f"😬 Narrow defeats (by 3 or fewer): {close_defeat_count} matches")
print(f"🚀 Biggest victory: {top_win['SU_Score']}-{top_win['Opponent_Score']} vs {top_win['Opponent']} on {top_win['Date']} (margin: {top_win['Score_Diff']})")
