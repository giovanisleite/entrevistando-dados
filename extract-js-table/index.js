const puppeteer = require('puppeteer')
const $ = require('cheerio')
const tableToCsv = require('node-table-to-csv')


const url = 'https://www.fipe.org.br/pt-br/indices/ipc/#indice-quadrissemanal&qultima'

puppeteer
  .launch()
  .then(function (browser) {
    return browser.newPage()
  })
  .then(function (page) {
    return page.goto(url).then(function () {
      return page.content()
    })
  })
  .then(function (html) {
    $('div#IpcQuadrUltimaInterna table.results', html).each(function () {
      console.log(tableToCsv(`<table>${$(this).html()}</table>`))
    })
  })
  .catch(function (err) {
    console.log('error')
  })
