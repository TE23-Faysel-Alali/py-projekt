def Hita_taggar_med_position(html):

    lista = []
    index = 0
    slut = len(html)

    body_start = html.find("<body")

    if body_start != -1:
        index = body_start
    else:
        index = 0

    while index < slut:

        start = html.find("<", index)
        if start == -1:
            break

        end = html.find(">", start)
        if end == -1:
            break

        tag = html[start+1:end]
        lista.append(tag)

        index = end + 1

    return lista




def Hitta_class_i_tag(tag):

    pos = tag.find('class="')

    if pos != -1:
        start = pos + 7
        end = tag.find('"', start)
        return tag[start:end]

    return ""




def Ta_bort_attribut(tag):

    mellan = tag.find(" ")

    if mellan != -1:
        return tag[:mellan]

    return tag




def Skapa_css_med_nesting(taggar):

    stack = []
    kombinationer = []

    for t in taggar:

        if t.startswith("!") or t.startswith("body") or t.startswith("/body"):
            continue


        # STÄNGANDE TAGG
        if t.startswith("/"):

            stangd = t[1:]
            stangd = Ta_bort_attribut(stangd)

            i = len(stack) - 1
            while i >= 0:

                if stack[i][0] == stangd:
                    stack.pop(i)
                    break

                i -= 1


        # ÖPPNANDE TAGG
        else:

            ren_tag = Ta_bort_attribut(t)
            class_namn = Hitta_class_i_tag(t)

            if class_namn != "":
                selector = "." + class_namn
            else:
                selector = ren_tag

            # spara både HTML-tagg och selector
            stack.append([ren_tag, selector])

            komb = ""

            for s in stack:
                komb += s[1] + " "

            komb = komb.strip()

            if komb not in kombinationer:
                kombinationer.append(komb)


    print("\n/* CSS MED RÄTT NESTING */\n")

    for k in kombinationer:
        print(k + " {")
        print("    ")
        print("}")
        print()




def main():

    html = """




<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsiv Sida</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Carl Marx</h1>
            <nav>
                <a href="#" class="active">Carl Marx</a>
                <a href="#">Rosa Luximburg</a>
                <a href="#">Fredic Engels</a>
                <a href="#">Vladmir Lenin</a>
                <a href="#">Che Geuvara</a>
            </nav>
        </header>
        <main>
            <h2>Om Carl Marx</h2>
            <img src="./bilder/image1.png" alt="">
            <p>Karl Marx (1818–1883) was a Prussian philosopher, economist, and revolutionary socialist whose critical analysis of capitalism and <br> theories on class struggle formed the basis of Marxism. Co-author of The Communist Manifesto (1848) with Friedrich Engels, he argued that history is driven by class conflict, predicting a worker revolution against capitalist oppression. </p>
        </main>
        <aside>
            <p><a href="https://www.marxists.org/archive/marx/works/1877/06/karl-marx.htm">Biogrofy</a></p>
            <p><a href="https://www.marxists.org/archive/marx/works/cw/index.htm">Collected Works</a></p>
        </aside>
        <footer>
            <p>Faisal Alali 2026</p>
        </footer>
    </div>
</body>
</html>




"""

    taggar = Hita_taggar_med_position(html)

    Skapa_css_med_nesting(taggar)



main()
