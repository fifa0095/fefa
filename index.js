const express = require('express');
const path = require('path');
const mongoose = require('mongoose')
const Generator = require('./script/Generator')

mongoose.connect('mongodb://localhost/notekb');
let db = mongoose.connection;




//Bring in models
let Article =require('./models/articles');
const bodyParser = require('body-parser');
const articles = require('./models/articles');


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
    Article.find({}, (e, articles)=>{
        if(e){
            console.log(e);
        }else{
            res.render('index', {
                title : 'Hello',
                articles : articles
            });
        }
    })
});

// Go to Game Route
app.get('/Story/Get', (req, res)=>{
    Article.findOne({Host : req.params.Host_id}, (e, article)=>{
        res.render('game', {
            Host_name : article.Host,
            Host_ID : article._id
        });
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
    Article.findOne({Host : req.params.id}, (e, article)=>{
        res.render('articles',{
            Text_body: Text1
        });
    });
    console.log("Fetch is working");
});

//Get 2nd Article
app.get('/STORY/:id/2', (req, res)=>{
    Article.findById(req.params.id, (e, article)=>{
        res.render('articles',{
            Text_body: Text2
        });
    });
});
//Get 3th Article
app.get('/STORY/:id/3', (req, res)=>{
    Article.findById(req.params.id, (e, article)=>{
        res.render('articles',{
            Text_body: Text3
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
    let article = new Article();
    article.Host = req.body.Host;
    article.Text1 = req.body.Text1;
    article.Text2 = req.body.Text2;
    article.Text3 = req.body.Text3;

    article.save( (e)=>{
        if(e){
            console.log(e);
            return;
        }else{
            res.send(article._id);
            
        }
    })
})

app.listen(3000, ()=>{
    console.log('Server started on port 3000.....');
});
