const express = require("express");

const app = express();
//to usen the contents in public directory


app.get("/", (req,res)=> {
	res.render("index.ejs");
});

// app.listen(3000,function(req,res){
// 	console.log("hourlyattendance app started")
// });
