const elements = require('./elements.js');

function calcIndent(text) {    
    for(let i = 0; i < text.length; i++)
        if(text[i] != ' ')
            return parseInt((i+2)/4);
    return 0;
}

function findOneOf(str,list,start) {
    let found = [];
    for(let i = 0; i < list.length; i++) {
        const j = str.indexOf(list[i],start);
        if(j != -1)
            found.push( { listIndex:i, index:j } );
    }
    return found.sort((a,b) => a.index - b.index)[0];
}

function findCodeBlocks(str) {
    let found = [];
    let start = 0;
    while(start != -1) {
        const j = str.indexOf('{',start);
        if(j != -1) {
            const k = str.indexOf('}',j);
            if(k != -1) {
                found.push( { start:j, end:k } );
                start = k+1;
            }
            else
                start = j+1;
        }
        else
            start = -1;
    }
    return found;
}

function findStrings(str) {
    let found = [];
    let start = 0;
    while(start != -1) {
        const j = str.indexOf('"',start);
        if(j != -1) {
            const k = str.indexOf('"',j+1);
            if(k != -1) {
                found.push( { start:j, end:k } );
                start = k+1;
            }
            else
                start = j+1;
        }
        else
            start = -1;
    }
    return found;
}

function findPairs(str,begin, end) {
    let pairs = [];
    let i = 0;
    while(i < str.length) {
        let j = findOneOf(str,begin,i);
        if(j == null) break;
        let k = str.indexOf(end[j.listIndex],j.index+1);
        if(k != -1) {
            pairs.push({listIndex:j.listIndex, begin:j.index, end:k});
            i = k+1;
        }
        else
            i = j.index+1;
    }
    return pairs;
}

function replaceSpaceswithPlaceholder(txt,pairs,replaceChar = "\u001F") {
    let result = txt;
    result = result.substring(0,pairs[0].begin);
    for(let i = 0; i < pairs.length; i++) {
        const str = txt.substring(pairs[i].begin,pairs[i].end+1).replace(/ /g,replaceChar);
        console.log(str);
        result += str;
        result += txt.substring(pairs[i].end+1,pairs[i+1]?pairs[i+1].begin:txt.length);
    }
    return result;
}

function replacePlaceholderwithSpace(txt,replaceChar = "\u001F") {
    return txt.replace(new RegExp(`${replaceChar}`, 'g'),' ');
}

function removeWhiteSpace(str) {
    return str.replace(/\s+/g, ' ');
}

// remove spaces around the equal sign
function trimEquals(str) {
    return str.replace(/\s*=\s*/g,'=');
}

const tokenize = (str) => str.split(/\s+/);

function tokenizeLine(line) {
    
    let begins = "{'\"";
    let ends = "}'\"";
    line = removeWhiteSpace(line);
    line = trimEquals(line);
    let codeBlocks = findCodeBlocks(line);
    let pairs = findPairs(line,begins,ends);    
    let pairswithoutSpaces = replaceSpaceswithPlaceholder(trimmedSpaces,pairs);
    let tokens = tokenize(pairswithoutSpaces);
    return tokens.map(x => replacePlaceholderwithSpace(x)).filter(x => x != '');
}

function tokenizeElement(line) {
    line = removeWhiteSpace(line);
    line = trimEquals(line);
    const name = line.split(' ')[0];
    let props = line.split(' ').slice(1);
    props = props.map(x => x[0] == "."?"class="+x.substring(1):x[0] == "#"?"id="+x.substring(1):"content="+x);
    props.forEach(x => console.log(x));
    props.forEach( (prop) => {
        const [key,value] = prop.split('=');
        console.log(key,value);
    });
    return {name,props};
}


// *****************************************************************************************************
// process1
// Get string and return list of lines and spaces
function process1(layout) {
    const lines = layout.split('\n');
    const list = [];
    for(const rawline of lines) {
        //const line = rawline.split('#')[0];
        const line = rawline;
        if(line.trim() == '') continue;
        const space = calcIndent(line);
        const attributes = line.trim().split(' ');
        const name = attributes[0];
        let props = null;
        if(attributes.length > 1)
            props = attributes.slice(-attributes.length+1);
        list.push({space,name,props,children:[]});
    }
    return list;
}

// *****************************************************************************************************
// process2
// Get list of lines and return root tree
function process2(list) {
    const root = {space: -1, name:'root', parent:null, children: []};
    let last_node = root;
    for(const node of list) {
        if(node.space == last_node.space) {
            last_node.parent.children.push(node);
            node.parent = last_node.parent;
        }
        else if(node.space > last_node.space) {
            last_node.children.push(node);
            node.parent = last_node;
        } else {
            let parent = last_node;
            while(parent.space >= node.space) {
                parent = parent.parent;
            }
            node.parent = parent;
            parent.children.push(node);
        }
        last_node = node;
    }
    return root;
}

// *****************************************************************************************************
// process3
// Get tree and return html
function process3(tree) {
    let html = "";
    let classes ="";
    let innerHTML = "";
    if(tree.name) {
        if(elements.hasOwnProperty(tree.name)) {
            const element = elements[tree.name];
            html+= element.start_tag.slice(0,-1);
            classes = element.classes;
        } else {
            html+= `<${tree.name}`;
        }
        
        if(tree.props) {
            for(const prop of tree.props) {
                const [key,value] = prop.split('=');
                if(value) {
                    if(key == 'class')
                        classes += " " + value.replace(/\+/g, ' ');
                    else
                        html+= ` ${key}="${value}"`;
                }
                else {
                    if(key.startsWith('.'))
                        classes += ` ${key.substring(1)}`;
                    else
                        innerHTML += `${key.replace(/_/g," ")}`;
                }
            }
        }
        if(classes)
            html+= ` class="${classes}"`;
        html+= ">" + innerHTML;
    }    
    for(const child of tree.children) {
        html+= process3(child);
    }
    if(tree.name) {
        if(elements.hasOwnProperty(tree.name)) {
            const element = elements[tree.name];
            html+= element.end_tag;
        } else {
            html+= `</${tree.name}>`;
        }
    }
    return html;
}

function parse(layout) {
    let list = process1(layout);

    let tree = process2(list);

    let html = process3(tree);

    return html;
}

class easyUI {
    init(layout,appid) {
        this.layout = layout;
        this.appid = appid;
        this.render(appid);
    }
    test() {
        console.log("test");
    }
    render(elementId) {
        let app_element = document.getElementById(elementId);
        const html = parse(this.layout);
        if(app_element) {
            app_element.innerHTML = html;
        } else {
            console.log(`app element ${elementId} not found`);
        }
    }    
}

module.exports =  {
    parse,
    easyUI,
    tokenizeElement
};
