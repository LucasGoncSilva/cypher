window.addEventListener('DOMContentLoaded', () => {

    function cypher(txt) {
        let text = txt
        let new_text = text.replace(/a/g, "A")
        new_text = new_text.replace(/c/g, "a")
        new_text = new_text.replace(/d/g, "D")
        new_text = new_text.replace(/e/g, "E")
        new_text = new_text.replace(/f/g, "F")
        new_text = new_text.replace(/g/g, "G")
        new_text = new_text.replace(/h/g, "H")
        new_text = new_text.replace(/i/g, "I")
        new_text = new_text.replace(/j/g, "J")
        new_text = new_text.replace(/k/g, "K")
        new_text = new_text.replace(/l/g, "L")
        new_text = new_text.replace(/m/g, "M")
        new_text = new_text.replace(/n/g, "N")
        new_text = new_text.replace(/p/g, "n")
        new_text = new_text.replace(/q/g, "m")
        new_text = new_text.replace(/r/g, "l")
        new_text = new_text.replace(/s/g, "k")
        new_text = new_text.replace(/t/g, "j")
        new_text = new_text.replace(/u/g, "i")
        new_text = new_text.replace(/v/g, "h")
        new_text = new_text.replace(/w/g, "g")
        new_text = new_text.replace(/x/g, "f")
        new_text = new_text.replace(/y/g, "e")
        new_text = new_text.replace(/z/g, "d")
        new_text = new_text.replace(/A/g, "c")
        new_text = new_text.replace(/D/g, "z")
        new_text = new_text.replace(/E/g, "y")
        new_text = new_text.replace(/F/g, "x")
        new_text = new_text.replace(/G/g, "w")
        new_text = new_text.replace(/H/g, "v")
        new_text = new_text.replace(/I/g, "u")
        new_text = new_text.replace(/J/g, "t")
        new_text = new_text.replace(/K/g, "s")
        new_text = new_text.replace(/L/g, "r")
        new_text = new_text.replace(/M/g, "q")
        new_text = new_text.replace(/N/g, "p")

        return new_text
    }

    document.getElementById('plain_txt').onkeyup = () => {

        let txt = document.getElementById('plain_txt').value
        document.getElementById('cyphed').value = cypher(txt)

    }

    document.getElementById('cyphed').onkeyup = () => {

        let txt = document.getElementById('cyphed').value
        document.getElementById('plain_txt').value = cypher(txt)

    }

})