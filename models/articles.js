let mongoose = require('mongoose');


//Article Schema

let articleSchema = mongoose.Schema({
    Host:{
        type:String,
        required: true
    },
    Text1:{
        type:String,
        required:true
    },
    Text2:{
        type:String,
        required:true
    },
    Text3:{
        type:String,
        required:true
    }
});

let Article = module.exports = mongoose.model('Article', articleSchema);