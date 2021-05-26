const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const https = require('https');
const axios = require('axios')
const PORT = 5000


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false
}))
app.use('/', express.static(__dirname + "/html")) //serve static content

const post_data = {
  "prime": "8c5508e356be4bb9564c0ae3a473baf023c32ff0d39960e336ddc25bb0c8cc27",
  "partner_key": "partner_SDmf75bmU83MLWX6HonFPCsCFnXDNEoutXEwtqjdxWzMGP8Q2UfCx9GI",
  "merchant_id": "HANWEN_TAISHIN",
  "details": "TapPay Test",
  "amount": 100,
  "cardholder": {
      "phone_number": "+886923456789",
      "name": "王小明",
      "email": "LittleMing@Wang.com",
      "zip_code": "100",
      "address": "台北市天龍區芝麻街1號1樓",
      "national_id": "A123456789"
  },
  "remember": false
}

axios.post('https://sandbox.tappaysdk.com/tpc/payment/pay-by-prime', post_data, {
  headers: {
      'x-api-key': 'partner_SDmf75bmU83MLWX6HonFPCsCFnXDNEoutXEwtqjdxWzMGP8Q2UfCx9GI'
  }
}).then((response) => {
  console.log("aaa",response.data);
  return res.json({
      result: response.data
  })
})

app.listen(PORT, () => {
    console.log('Connet your webiste in the http://localhost:3000/');
})