const sortingHelper = (arr)=>
{
  let x=  arr.sort((a,b)=> a-b)
  let res = x.map(i=>i*i)
    return res
}

test  = sortingHelper([6,4,1,2,3,5])
console.log(test)