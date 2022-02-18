function perimeter(n) {
    let pcs = n+1;
    var i,sum;
    var fib = []; fib[0] = 0; fib[1] = 1;
  
    for (i = 2; i <= pcs; i++) {
      fib[i] = fib[i - 2] + fib[i - 1];
    }
  
    let calc = () =>{
      sum =fib.reduce((a,b)=>a+b,0)
      console.log(sum)
      }
    
    calc();
    
    return sum*4
    }
