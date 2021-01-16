let carts=document.querySelectorAll('.add-btn');

let products=[
    {
        name:'BBQ',
        price:150,
        incart:0
    },
    {
        name:'tanduri chicken',
        price:160,
        incart:0
    },
    {
        name:'Body building plan',
        price:155,
        incart:0
    },
    {
        name:'BBQ2',
        price:140,
        incart:0
    }
];

for (let i = 0; i < carts.length; i++) {
    carts[i].addEventListener('click',()=>{
        cartNumber(products[i]);
        totalcost(products[i]);
        window.location.reload();
    })
    
}

function onLoadCartNumber(){
   
    let productnumber=localStorage.getItem('cartNumber');
    
    if(productnumber){
        document.querySelector('.item strong').textContent=productnumber;
    
        }

    
}

function cartNumber(product)
{    
    let productnumber=localStorage.getItem('cartNumber');
    let cartcost=localStorage.getItem('totalcost');
    productnumber=parseInt(productnumber);
    if(productnumber){
    
    localStorage.setItem('cartNumber',productnumber+1);
    document.querySelector('.item strong').textContent=productnumber+1;


    }
    else{

    localStorage.setItem('cartNumber',1);
    document.querySelector('.item strong').textContent=1;
    }

    setItems(product);
    
}
function setItems(product){
    let cartitems=localStorage.getItem('productsincart');
    cartitems=JSON.parse(cartitems);
    if(cartitems!=null){
        if(cartitems[product.name]==undefined){
            cartitems={
                ...cartitems,
                [product.name]:product
            }
        }
        cartitems[product.name].incart+=1;
    }
    else{
    product.incart=1;
    cartitems={
        [product.name]:product
    }
}
    localStorage.setItem("productsincart", JSON.stringify(cartitems));
    
}
function totalcost(product){
    let cartcost=localStorage.getItem('totalcost');

    if(cartcost!=null){
        cartcost=parseInt(cartcost);
        localStorage.setItem('totalcost',cartcost + product.price);
        
    }
    else{
        localStorage.setItem('totalcost',product.price);
    }
}

function display()
{
    let cartitems=localStorage.getItem('productsincart');
    
    cartitems=JSON.parse(cartitems);
    console.log(cartitems);
    let productcontainer=document.querySelector('.products');
    let cartcost=localStorage.getItem('totalcost');
    console.log("total cost",cartcost);
    console.log("data ",cartitems);
    if(cartitems && productcontainer ){
        console.log("running");
        
        document.querySelector('.total strong').textContent=cartcost;
        productcontainer.innerHTML = '';
        Object.values(cartitems).map(item=>{
            productcontainer.innerHTML += '<tr><td>'+item.name +'</td><td>'+'<input type="button" class="btn btn-add btn-success btn-sm" value="+"></input>'+' '+item.incart+' '+'<input type="button" class="btn btn-minus btn-danger btn-sm" value="-"></input>'+'</td><td>'+(item.price)*(item.incart) +'</td><td>'+'<input type="button" class="btn btn-del btn-danger btn-sm" value="Delete"></input>' +'</td></tr>'
        });
    } 
    
}
onLoadCartNumber();
display();