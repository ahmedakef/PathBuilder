class Slugit {

    slugFunc(text, owner){

        var isCalled = owner["Slugit"] != "Slugit"

        if(isCalled) {
            throw new ReferenceError('slugFunc cannot be implemented!');
            return false;
        }
        var char_map = {
            'Ç' : 'c', 'ç' : 'c', 'Ğ' : 'g', 'ğ' : 'g',
            'Ş' : 's', 'ş' : 's', 'Ü' : 'u', 'ü' : 'u',
            'Ö' : 'o', 'ö' : 'o', 'ı' : 'i'
        }

        text = text.replace(/[^\w ]/g, function(char) {
        return char_map[char] || char;
        });

        return text.toString().toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w\-]+/g, '')
        .replace(/\-\-+/g, '-')
        .replace(/^-+/, '')
        .replace(/-+$/, '');
    }

    doSlug(data) {
        
        var el = document.querySelector(data.el)
        var target = document.querySelector(data.target)
        
        var elems = ["form", "input", "textarea", 
                        "select", "option", "button"]
        
        var isFormElem = elems.indexOf(target.tagName.toLowerCase())

        el.addEventListener(data.event, function() {
            setTimeout(function() {
                if(isFormElem > 0) {
                    target.value = Slugit.prototype.slugFunc(el.value, {Slugit: "Slugit"})
                } else {
                    target.innerText = Slugit.prototype.slugFunc(el.value, {Slugit: "Slugit"})
                }
            }, data.timeout)
        })
    }
}


// source : https://github.com/aligoren/Slugit.js