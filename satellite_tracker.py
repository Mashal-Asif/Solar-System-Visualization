from skyfield import api
from pytz import timezone
import matplotlib.pyplot as plt
import numpy as np

# -------------------------------
# Timezone
# -------------------------------
time_zone = timezone('US/Pacific')

# -------------------------------
# Load ISS TLE data
# -------------------------------
station_data = api.load.tle('https://celestrak.org/NORAD/elements/stations.txt')
iss = station_data['ISS (ZARYA)']
print(iss)

# -------------------------------
# Time setup
# -------------------------------
time_scale = api.load.timescale()

minutes = range(60 * 24 * 2)  # 2 days
time_range = time_scale.utc(2024, 3, 21, 2, minutes)

# -------------------------------
# Observer location
# -------------------------------
location = api.Topos(latitude='20.3123 S', longitude='118.64498 E')

# -------------------------------
# Orbit calculation
# -------------------------------
orbit = (iss - location).at(time_range)
altitude, azimuth, distance = orbit.altaz()

print(f"Altitudes: {altitude}")
print(f"Azimuth: {azimuth}")
print(f"Distance: {distance}")

# -------------------------------
# Visibility mask
# -------------------------------
visible = altitude.degrees > 0

# -------------------------------
# Detect rise/set transitions (SAFE METHOD)
# -------------------------------
rise = np.where((~visible[:-1]) & (visible[1:]))[0]
set_ = np.where((visible[:-1]) & (~visible[1:]))[0]

# Ensure pairs match
n = min(len(rise), len(set_))
rise = rise[:n]
set_ = set_[:n]

passes = list(zip(rise, set_))
print("Detected passes:", passes)

# -------------------------------
# Choose a pass
# -------------------------------
if len(passes) == 0:
    print("No visible ISS passes in this time range.")
    exit()

pass_to_observe = 0
rise_idx, set_idx = passes[pass_to_observe]

print(f"ISS Rises at {time_range[rise_idx].astimezone(time_zone)}")
print(f"ISS Sets at {time_range[set_idx].astimezone(time_zone)}")

# -------------------------------
# Polar plot
# -------------------------------
ax = plt.subplot(111, projection='polar')
plt.title("ISS Pass Polar Chart")

ax.set_rlim(0, 90)
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)

theta = azimuth.radians
r = 90 - altitude.degrees

# Plot selected pass
ax.plot(theta[rise_idx:set_idx], r[rise_idx:set_idx], 'bo--')

# Add labels
step = max(1, (set_idx - rise_idx) // 10)

for k in range(rise_idx, set_idx, step):
    text = time_range[k].astimezone(time_zone).strftime('%H:%M')
    ax.text(theta[k], r[k], text, fontsize=8)

plt.show()