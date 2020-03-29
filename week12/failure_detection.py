def freefall_detect(acc_total,acc_time, threshold = 15, window = 3):
    for i in range(len(acc_total)):
        if(i < window - 1):
            continue
        w_sum = 0
        for j in range(0, window):
            w_sum += acc_total[i - j]
        w_avg = w_sum / window
        rate = abs(acc_total[i] - w_avg)
        if rate > threshold:
            time = acc_time[i]
            print("Fall Detected at: "+str(time)+" seconds!")
            return time
    return -1

if __name__ == "__main__":
    acc_time = [1.1,1.2,1.3,1.4,1.5]
    acc_total = [1,2,3,4,60]
    freefall_detect(acc_total,acc_time)