

def Hita_klass_namn(html):
    n = len(html)
    klass_namn_lista = []
    klass_namn = ''
    index_b = 0
    index_s = len(html)
    klass_b = 0

    while klass_b != (-1):
        
        klass_b = html.find('<', index_b, index_s)

        if klass_b != (-1):
            klass_s = html.find('>', klass_b, index_s)

            print(html.find('/', klass_b, klass_s))

            
            if html.find('/', klass_b, klass_s) != -1:
                #Gör att den inte s
                
                pass
            else: 
                
                for j in range(klass_s - (klass_b + 1)):
                    klass_namn += (html[klass_b + 1 + j])

                klass_namn_lista.append(klass_namn)
                klass_namn = ''

                print(klass_b)
                print(index_b)
                print(klass_namn_lista)

            index_b = klass_s

    return klass_namn_lista
    









def main ():
    #html = input("Klistra in din html")

    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neon Cowboy Bebop</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="contaner">
        <header>
            <h1>Neon Cowboy Bebop</h1>
            <h2>A place where you can peafuly goon</h2>
            <nav>
                <a class="active" href="#">Home</a>
                <a href="#">Gay Reels</a>
                <a href="#">About Cowboy Bebop</a>
                <a href="#">Find Me 😝</a>
            </nav>
        </header>
"""
    namn_lista = Hita_klass_namn (html)
    print(namn_lista)
    
    




main()




