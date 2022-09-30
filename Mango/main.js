const express = require('express');
const app = express();

const mongoose = require('mongoose');    
mongoose.connect('mongodb://localhost/main', { useNewUrlParser: true, useUnifiedTopology: true });    //1~6 이용자가 저장한 쿼리값 반환
const db = mongoose.connection;

// flag is in db, {'uid': 'admin', 'upw': 'DH{32alphanumeric}'}
const BAN = ['admin', 'dh', 'admi'];

filter = function(data){
    const dump = JSON.stringify(data).toLowerCase();
    var flag = false;
    BAN.forEach(function(word){
        if(dump.indexOf(word)!=-1) flag = true;
    });
    return flag;
}

app.get('/login', function(req, res) {
    if(filter(req.query)){
        res.send('filter');
        return;
    }
    const {uid, upw} = req.query;

    db.collection('user').findOne({
        'uid': uid,
        'upw': upw,
    }, function(err, result){
        if (err){
            res.send('err');
        }else if(result){
            res.send(result['uid']);
        }else{
            res.send('undefined');
        }
    })
});

app.get('/', function(req, res) {                // 빈 페이지에서 출력될 내용을 결정하는 코드    //페이로드 생성 = 공격을 위해 임의의 데이터를 삽입한다.
    res.send('/login?uid=guest&upw=guest');
});

app.listen(8000, '0.0.0.0');


