# The Monte Carlo method estimates quantities using random sampling.
# To estimate π, sample random points in the square [-1, 1] × [-1, 1]
# and count the fraction that fall inside the unit circle (x^2 + y^2 ≤ 1).
# This fraction approximates the area ratio π/4, so π ≈ 4 × (inside/total).

import asyncio
import random

async def monte_carlo(num_points):
    inside_circle = 0  # count of points that fall inside the unit circle

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            inside_circle += 1
    return inside_circle, num_points  # (inside_circle, total_points_in_task)

# Run multiple tasks to improve the estimate—the more samples, the better
async def estimate_pi(total_points, tasks):
    # total_points: total number of random points to sample
    # tasks: number of async tasks to split the work into
    points_per_task = total_points // tasks  # remainder is ignored

    coroutines = [monte_carlo(points_per_task) for _ in range(tasks)]
    results = await asyncio.gather(*coroutines)  # run tasks concurrently

    # r[0] and r[1] because monte_carlo returns (inside_circle, num_points)
    total_inside_circle = sum(r[0] for r in results)
    total_points_used = sum(r[1] for r in results)

    pi = 4 * (total_inside_circle / total_points_used)  # area ratio: pi/4 ≈ inside/total
    return pi

async def main():
    total_points = 20000999  # more points -> more accurate
    tasks = 20

    pi = await estimate_pi(total_points, tasks)
    print(f"Pi approximation: {pi}")

asyncio.run(main())
