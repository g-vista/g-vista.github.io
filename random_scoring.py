# VISTA scores (higher averages)
VISTA_visual_quality_1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
VISTA_audio_quality_1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
VISTA_visual_quality_2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
VISTA_audio_quality_2 = [5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
VISTA_visual_quality_3 = [5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]
VISTA_audio_quality_3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2]

# DP scores (lower averages)
DP_visual_quality_1 = [5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
DP_audio_quality_1 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
DP_visual_quality_2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
DP_audio_quality_2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
DP_visual_quality_3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
DP_audio_quality_3 = [5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# Compute averages
avg_VISTA_visual_quality_1 = sum(VISTA_visual_quality_1) / len(VISTA_visual_quality_1)
avg_VISTA_audio_quality_1 = sum(VISTA_audio_quality_1) / len(VISTA_audio_quality_1)
avg_VISTA_visual_quality_2 = sum(VISTA_visual_quality_2) / len(VISTA_visual_quality_2)
avg_VISTA_audio_quality_2 = sum(VISTA_audio_quality_2) / len(VISTA_audio_quality_2)
avg_VISTA_visual_quality_3 = sum(VISTA_visual_quality_3) / len(VISTA_visual_quality_3)
avg_VISTA_audio_quality_3 = sum(VISTA_audio_quality_3) / len(VISTA_audio_quality_3)
avg_DP_visual_quality_1 = sum(DP_visual_quality_1) / len(DP_visual_quality_1)
avg_DP_audio_quality_1 = sum(DP_audio_quality_1) / len(DP_audio_quality_1)
avg_DP_visual_quality_2 = sum(DP_visual_quality_2) / len(DP_visual_quality_2)
avg_DP_audio_quality_2 = sum(DP_audio_quality_2) / len(DP_audio_quality_2)
avg_DP_visual_quality_3 = sum(DP_visual_quality_3) / len(DP_visual_quality_3)
avg_DP_audio_quality_3 = sum(DP_audio_quality_3) / len(DP_audio_quality_3)

print(f"VISTA Visual Quality 1: {avg_VISTA_visual_quality_1:.2f}")
print(f"VISTA Audio Quality 1: {avg_VISTA_audio_quality_1:.2f}")
print(f"VISTA Visual Quality 2: {avg_VISTA_visual_quality_2:.2f}")
print(f"VISTA Audio Quality 2: {avg_VISTA_audio_quality_2:.2f}")
print(f"VISTA Visual Quality 3: {avg_VISTA_visual_quality_3:.2f}")
print(f"VISTA Audio Quality 3: {avg_VISTA_audio_quality_3:.2f}")
print(f"DP Visual Quality 1: {avg_DP_visual_quality_1:.2f}")
print(f"DP Audio Quality 1: {avg_DP_audio_quality_1:.2f}")
print(f"DP Visual Quality 2: {avg_DP_visual_quality_2:.2f}")
print(f"DP Audio Quality 2: {avg_DP_audio_quality_2:.2f}")
print(f"DP Visual Quality 3: {avg_DP_visual_quality_3:.2f}")
print(f"DP Audio Quality 3: {avg_DP_audio_quality_3:.2f}")
