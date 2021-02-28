const express = require('express');
const path = require('path');
const mongoose = require('mongoose')
const Generator = require('./script/Generator')

mongoose.connect('mongodb://localhost/mail');
let db = mongoose.connection;




//Bring in models
let Article =require('./models/articles');
const bodyParser = require('body-parser');


// Check connection
db.once('open', ()=>{
    console.log('Connected to ManogoDB')
})


//check for db errors
db.on('error',(e)=>{
    console.log(e)
})

// Init App
const app = express();


//Body Parser Middleware
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({extended:false}))

//parse application/json
app.use(bodyParser.json())


// Set Public Folder
app.use(express.static(path.join(__dirname, 'public')));

// Load View Engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine','pug');

//app.use(express.json);

//Home Route
app.get('/', (req,res)=>{
    /*res.render('index', {
        title : 'Hello'
    });*/
    console.log("Fetch is Worked");
});

// Go to Game Route
app.get('/Story/Get', (req, res)=>{
    res.render('game', {
        Host_name : req.body.Host
    });
});

// Add Route
app.get('/Story/add', (req,res)=>{
    res.render('add', {
        title : 'Story'
    });
});

//Get Single Article
//Get 1st Article
app.get('/STORY/:id/1', (req, res)=>{
    Article.findById(req.params.id, (e, article)=>{
        res.render('article',{
            Text1: Text1,
            Text2: Text2,
            Text3: Text3
        });
    });
});
//Get 2nd Article
app.get('/STORY/:id/2', (req, res)=>{
    Article.findById(req.params.id, (e, article)=>{
        res.render('article',{
            Text1: Text1,
            Text2: Text2,
            Text3: Text3
        });
    });
});
//Get 3th Article
app.get('/STORY/:id/3', (req, res)=>{
    Article.findById(req.params.id, (e, article)=>{
        res.render('article',{
            Text1: Text1,
            Text2: Text2,
            Text3: Text3
        });
    });
});

//Game Route
app.get('/Game', (req, res)=>{
    const charac = Generator()
    res.render('game',{
        C1 : charac[0],  
        C2 : charac[1],  
        C3 : charac[2],  
        C4 : charac[3]  
    });
});


//Add Submit POST Route
app.post('/Story/add', (req,res)=>{
    let articles = new Article();
    articles.Host = req.body.Host;
    articles.Text1 = req.body.Text1;
    articles.Text2 = req.body.Text2;
    articles.Text3 = req.body.Text3;

    articles.save( (e)=>{
        if(e){
            console.log(e);
            return;
        }else{
            res.redirect('/');
        }
    })
})

app.listen(3000, ()=>{
    console.log('Server started on port 3000.....');
});
