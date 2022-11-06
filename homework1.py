# Name: Tianjiao Xu

# In this assignment, we will practice using sorting and list comprehensions.

## Feel free to use the following global variable alphabet
import math
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Problem 1.

def build_cipher(shift):
    """
    >>> build_cipher(-3)
    {'a': 'x', 'b': 'y', 'c': 'z', 'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g', 'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't', 'x': 'u', 'y': 'v', 'z': 'w'}

    >>> build_cipher(-1)
    {'a': 'z', 'b': 'a', 'c': 'b', 'd': 'c', 'e': 'd', 'f': 'e', 'g': 'f', 'h': 'g', 'i': 'h', 'j': 'i', 'k': 'j', 'l': 'k', 'm': 'l', 'n': 'm', 'o': 'n', 'p': 'o', 'q': 'p', 'r': 'q', 's': 'r', 't': 's', 'u': 't', 'v': 'u', 'w': 'v', 'x': 'w', 'y': 'x', 'z': 'y'}
    
    Parameters
    ----------
    shift : TYPE
        the funtction that give a  shift to 26 alphabet number.

    Returns
    -------
    None.

    """
    dic= {}
    for i in range(len(alphabet)):
        if i+shift <= len(alphabet)-1:
            dic[alphabet[i]]=alphabet[i+shift]
        else:
            dic[alphabet[i]]=alphabet[i+shift-len(alphabet)]
    return dic

# Problem 2
def encode(text, shift):
    """
    >>> encode("abcd", -3)
    'xyza'
    
    >>> encode("abcd", -1)
    'zabc'
    
    
    Parameters
    ----------
    text : TYPE
        encode.
    shift : TYPE
        use shift to change number

    Returns
    -------
    None.

    """
    encoded=''
    for i in text:
        encoded+=(build_cipher(shift))[i]
    return encoded

    

# Problem 3

def decode(text, cipher):
    """
    >>> decode("xyza", -3)
    'abcd'
    >>> decode("zabc", -1)
    'abcd'
    
    Parameters
    ----------
    text : TYPE
        string.
    cipher : TYPE
        do decode by cipher dictionary.

    Returns
    -------
    None.

    """
    decoded=''
    for i in text:
        if i.islower():
            if i in build_cipher(-cipher):
                new = build_cipher(-cipher)[i]
                decoded = decoded + new
        else:
            decoded+=i
    return decoded

# Problem 4
def remove_extraneous(text):
    """
    >>> remove_extraneous("thr/")
    'thr'
    
    >>> remove_extraneous("boo!")
    'boo'
    
    Parameters
    ---------- 
    text : TYPE
        only keep alphanet

    Returns
    -------
    None.

    """
    newstring="" 
    for i in text:
       if(i.isalpha()): 
           newstring+=i
    return(newstring)

# Problem 5
def character_frequency(text):
    """
    >>> character_frequency("hello world!")
    {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

    >>> character_frequency("aaa")
    {'a': 3}
    
    
    Parameters
    ----------
    text : TYPE
        times that alphabet experience.

    Returns
    -------
    None.

    """
    dic={}
    l=list(text)
    for i in l:
        if i in alphabet:
            dic[i]=l.count(i)
    return dic

# Problem 6
def character_frequency_string(text):
    """
    >>> character_frequency_string("hello world")
    a
    b
    c
    d *
    e *
    f
    g
    h *
    i
    j
    k
    l ***
    m
    n
    o **
    p
    q
    r *
    s
    t
    u
    v
    w *
    x
    y
    z

    Parameters
    ----------
    text : TYPE
        string.

    Returns
    -------
    i : TYPE
        test frequency.

    """
    for i in alphabet:
        if i in text:
            print(i,(character_frequency(text)[i])*'*')
        else:
            print(i)
    

# Problem 7
text = "Tmjwj tshj bfx f kfwr bnym f gnl wji gfws. Asi ns ymfy gnl wji gfws, ymjwj qnaji rfsd fsnrfqx, ymj xrfqqjxy tk bmnhm, bfx f qnyyqj wji mjs. Tmj qnyyqj wji mjs rfd mfaj gjjs qnyyqj, gzy xmj bfx ymj rtxy fhynaj wjxnijsy tk ymj kfwr. Wmjs xmj bfxs'y qfdnsl jllx, xmj xujsy mjw ynrj hqzhpnsl fsi bfqpnsl fgtzy ymj gfws, ujhpnsl fy ymj xjjix ts ymj lwtzsi, tw lfymjwnsl zu ybnlx fsi mfd yt rfpj mjw sjxy. Smj pjuy jajwdymnsl ns ymj gfws ynid fsi hqjfs."
print(character_frequency_string(text))
print(ord('j'))
print(ord('e'))
print(decode(text, 5))



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    print(build_cipher(-3))
    print(build_cipher(-1))
    print(encode("abcd", -3))
    print(encode("abcd", -1))
    print(decode("xyza", 3))
    print(decode("zabc", 1))
    print(remove_extraneous("thr/"))
    print(remove_extraneous("boo!\n"))
    print(character_frequency("hello world!"))
    print(character_frequency("aaa"))
    print(character_frequency_string("hello world"))
    
