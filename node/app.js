import express from 'express';

const app=express()
const port=3000

app.get('/',(req,res)=>{
   res.send("Hello Docker khan")
   console.log('hello docker')
})


app.listen(port,()=>{
  console.log(`run server in port :${port}`)
})


//! Docker
//* start and stop contaner by ID 