def win_probability(x, y):
    return y / (x + y)

def round_one_prob(x, y):
    return win_probability(x, y)

def round_two_prob(x, a, b):
    xwinA = a / (x + a) * round_one_prob(a, b)
    xwinB = b / (x + b) * round_one_prob(b, a)
    return xwinA + xwinB

def round_three_prob(x, a, b, c, d):
    xwinA = a / (x + a) * round_two_prob(a, c, d) * round_one_prob(a, b)
    xwinB = b / (x + b) * round_two_prob(b, c, d) * round_one_prob(b, a)
    xwinC = c / (x + c) * round_two_prob(c, a, b) * round_one_prob(c, d)
    xwinD = d / (x + d) * round_two_prob(d, a, b) * round_one_prob(d, c)
    return xwinA + xwinB + xwinC + xwinD

def round_four_prob(x, a, b, c, d, e, f, g, h):
    xwinA = a / (x + a) * round_three_prob(a, e, f, g, h) * round_two_prob(a, c, d) * round_one_prob(a, b)
    xwinB = b / (x + b) * round_three_prob(b, e, f, g, h) * round_two_prob(b, c, d) * round_one_prob(b, a)
    xwinC = c / (x + c) * round_three_prob(c, e, f, g, h) * round_two_prob(c, a, b) * round_one_prob(c, d)
    xwinD = d / (x + d) * round_three_prob(d, e, f, g, h) * round_two_prob(d, a, b) * round_one_prob(d, c)
    xwinE = e / (x + e) * round_three_prob(e, a, b, c, d) * round_two_prob(e, g, h) * round_one_prob(e, f)
    xwinF = f / (x + f) * round_three_prob(f, a, b, c, d) * round_two_prob(f, g, h) * round_one_prob(f, e)
    xwinG = g / (x + g) * round_three_prob(g, a, b, c, d) * round_two_prob(g, e, f) * round_one_prob(g, h)
    xwinH = h / (x + h) * round_three_prob(h, a, b, c, d) * round_two_prob(h, e, f) * round_one_prob(h, g)
    return xwinA + xwinB + xwinC + xwinD + xwinE + xwinF + xwinG + xwinH

def win_chance(format):
    r1 = round_one_prob(format[14], format[15])
    r2 = round_two_prob(format[14], format[12], format[13])
    r3 = round_three_prob(format[14], format[11], format[10], format[9], format[8])
    r4 = round_four_prob(format[14], format[7], format[6], format[5], format[4], format[3], format[2], format[1], format[0])
    return r1 * r2 * r3 * r4
    

def best_swap():
    format = [ 1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
    base_probability = win_chance(format)
    besti = None
    bestj = None
    bestProb = base_probability
    for i in range(16):
        if i == 14:
            continue
        for j in range(i+1, 16):
            order = [ 1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
            if j == 14:
                continue
                
            order[i], order[j] = order[j], order[i]
            newProb = win_chance(order)   
            
            print(order, i, j, newProb)
            
            if newProb > bestProb:
                bestProb = newProb
                besti = i
                bestj = j
    
    print("Best swap: " + format[besti] + " and " + format[bestj])
    print("Probability increase : " bestProb - base_probability)