<template>
  <v-container>
    <v-row class="text-center">
      <v-col
       class="mb-4"
       cols="7"
      >
      <div id="word-cloud"></div>
      </v-col>

      <v-col
       class="mb-4"
       cols="5"
      >
        <v-data-table
        :headers="headers"
        :items="newss"
        sort-by="create_date"
        sort-desc="true"
        class="elevation-1"
        :items-per-page="10"
        :hide-default-footer="true"
        @click:row="serverPage"
        >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title
              >주요 뉴스
              <span v-if="keyname" class="body-1 font-italic ml-3"
                >(with {{ keyname }} tagged)</span
              >
            </v-toolbar-title>
          </v-toolbar>
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

  export default {
    name: 'HelloWorld',

    data: () => ({
      newss: [],
      keywords: [],
      keyname: "",
      headers: [
        { text: "제 목", value: "title" },
        { text: "분 야", value: "category" },
        { text: "작성일", value: "create_date" },
        { text: "언론사", value: "press" },
      ],
    }),
    created() {
      this.fetchKeywords();
    },
    methods: {
      fetchNewsList() {
        console.log("fetchNewsList()...", this.keywords);

        const max = this.keywords.reduce(function(prev, current) {
          return (prev.count > current.count) ? prev : current
        })
        console.log("find max count...", this.keyname);
        this.keyname = max.name;

        let getUrl = "";
        if (this.keyname) getUrl = `/api/news/list/?keyname=${this.keyname}`;
        else getUrl = "/api/news/list";

        axios
        .get(getUrl)
        .then((res) => {
          console.log("NEWS LIST GET RES!!", res);
          this.newss = res.data;
        })
        .catch((err) => {
          console.log("NEWS LIST ERR RES!!", err.response);
          alert(err.response.status + "" + err.response.statusText);
        });
      },
      serverPage(item) {
        console.log("serverPage()...", item);
        location.href = `/blog/news/${item.id}`;
      },

      

      fetchKeywords() {
        console.log("fetchKeywords()..");
        axios.get('/api/keyword/cloud/')
        .then(res => {
          console.log("NEWS CLOUD GET RES", res);
          this.keywords = res.data;
          //tag.weight
          //배열의 각 원소에 조작하려면 forEach 매서드를 사용할 수 있다.
          this.fetchNewsList();
          this.genKeycloud();
        })
        .catch(err => {
          console.log("KEY CLOUD GET ERR.RESPONSE", err.response);
          alert(err.response.status+ ''+ err.response.statusText);
        });
      },
      genKeycloud() {
        console.log("genKeycloud()..", this.keywords);
        const d3 = require('d3');
        wordScale = d3.scale.linear().domain([0, 500]).range([0, 50]).clamp(true);
        //const cloud = require('d3-cloud');
        d3.layout.cloud()
          .words(this.keywords)
          .padding(5)
          .font('Impact')
          .rotate(0)
          .text((d) => d.name)
          .fontSize(function(d) {return wordScale(d.count);})
          .on('end', this.end)
          .spiral('archimedean')
          .start()
          .stop()
      },
      end(words) {
        console.log("end function...", words);
        const d3 = require('d3');
        const width = 800;
        const height = 800;
        d3.select('#word-cloud')
          .append('svg')
          .attr('width', width)
          .attr('height', height)
          .style('background', 'white')
          .append('g')
          .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')') // g를 중심에서 단어들을 그리기 때문에 g를 svg 중심으로 이동
          .selectAll('text')
          .data(words)
          .enter()
          .append('text')
          .style('font-size', (d) => {
            return d.size + "px";
          })
          .style('font-family', 'Impact')
          .style('opacity', 0.8)
          .attr('text-anchor', 'middle')
          .attr('transform', (d) => {
            return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
          })
          .text((d) => d.name)        
          .on("click", function() {
              const sltKey = d3.select(this).text();
              serverPagewithTag(sltKey);
            })
          function serverPagewithTag(keyname) {
            console.log("serverPagewithTag()...", keyname);
            location.href = `/blog/news/list/?keyname=${keyname}`;
          }
      },
      
    }
  }
</script>

<style scoped>
.v-data-table >>> tbody > tr {
  cursor: pointer;
}
</style>