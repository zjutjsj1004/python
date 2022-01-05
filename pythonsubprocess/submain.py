import sys
 

if __name__ == "__main__":
    param = sys.argv[1]
    if param == "0":
        sys.stdout.write("input 0")
        sys.exit(0)
    else:
        sys.stderr.write('5002')
        sys.exit(255)                        # 因为返回值main在UNIX 上被限制在[0, 255] 范围内， 我们返回256，会使得变成0。 不过可以通过stdout和stderr输出
    


    

