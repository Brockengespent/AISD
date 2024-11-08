import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    def closest_pair_rec(px, py):
        if len(px) <= 3:
            return min((distance(px[i], px[j]), (px[i], px[j]))
                       for i in range(len(px)) for j in range(i + 1, len(px)))
        
        mid = len(px) // 2
        Qx = px[:mid]
        Rx = px[mid:]
        
        midpoint = px[mid][0]
        Qy = list(filter(lambda x: x[0] <= midpoint, py))
        Ry = list(filter(lambda x: x[0] > midpoint, py))
        
        (d1, pair1) = closest_pair_rec(Qx, Qy)
        (d2, pair2) = closest_pair_rec(Rx, Ry)
        
        d = min(d1, d2)
        if d == d1:
            best_pair = pair1
        else:
            best_pair = pair2
        
        strip = [p for p in py if abs(p[0] - midpoint) < d]
        
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                p, q = strip[i], strip[j]
                dst = distance(p, q)
                if dst < d:
                    d = dst
                    best_pair = (p, q)
        
        return d, best_pair
    
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(px, py)

def main():
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        points = [tuple(map(int, file.readline().strip().split())) for _ in range(n)]
    
    min_distance, _ = closest_pair(points)
    
    with open('output.txt', 'w') as file:
        file.write(f"{min_distance:.4f}\n")

if __name__ == "__main__":
    main()
