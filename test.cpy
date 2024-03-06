def main_countdigits():
#{
    #declare x, count
    #$ x = int(input()); #$
    x = 5;
    count = 0;
    if (x>0):
    #{
        x = x // 10;
        count = count + 1;
    #}
    print(count);
#}

if __name__ == "__main__":
main_countdigits();