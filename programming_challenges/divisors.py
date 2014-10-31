def divisors(n):
    """Return the divisors of an integer number $n$."""
    if not isinstance(n, (int, long)):
        raise Exception("The input should be an integer number.")
        
    div = [1]
    if n==1:
        return div
    else:
        for i in range(2, int(n/2) + 1):
            if n%i == 0:
                div.append(i)
        div.append(n)
        return div


if __name__ == "__main__":
    
    # [1, 2, 3, 4, 6, 12]
    print divisors(12)
    
    # [1, 2, 4, 5, 10, 20, 25, 50, 100]
    print divisors(100)
    
    # Error
    print divisors(43.4)
