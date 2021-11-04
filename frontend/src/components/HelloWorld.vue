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
        :items="posts"
        sort-by="name"
        class="elevation-1"
        :items-per-page="10"
        :hide-default-footer="true"
        @click:row="serverPage"
        >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title
              >주요 뉴스
              <span v-if="tagname" class="body-1 font-italic ml-3"
                >(with {{ tagname }} tagged)</span
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
      posts: [],
      tagwords: [],
      tagname: "",
      headers: [
        {
          text: "ID",
          align: "start",
          sortable: false,
          value: "id",
        },
        { text: "제 목", value: "title" },
        { text: "요 약", value: "description" },
        { text: "수정일", value: "modify_dt" },
        { text: "작성자", value: "owner" },
        { text: "Actions", value: "actions", sortable: false },
      ],
    }),
    created() {
      this.fetchTags();
    },
    methods: {
      fetchPostList() {
        console.log("fetchPostList()...", this.tagwords);

        const max = this.tagwords.reduce(function(prev, current) {
          return (prev.count > current.count) ? prev : current
        })
        console.log("find max count...", this.tagname);
        this.tagname = max.name;

        let getUrl = "";
        if (this.tagname) getUrl = `/api/post/list/?tagname=${this.tagname}`;
        else getUrl = "/api/post/list";

        axios
        .get(getUrl)
        .then((res) => {
          console.log("POST LIST GET RES!!", res);
          this.posts = res.data;
        })
        .catch((err) => {
          console.log("POST LIST ERR RES!!", err.response);
          alert(err.response.status + "" + err.response.statusText);
        });
      },
      serverPage(item) {
        console.log("serverPage()...", item);
        location.href = `/blog/post/${item.id}`;
      },

      

      fetchTags() {
        console.log("fetchTags()..");
        axios.get('/api/tag/cloud/')
        .then(res => {
          console.log("POST CLOUD GET RES", res);
          this.tagwords = res.data;
          //tag.weight
          //배열의 각 원소에 조작하려면 forEach 매서드를 사용할 수 있다.
          this.fetchPostList();
          this.genTagcloud();
        })
        .catch(err => {
          console.log("TAG CLOUD GET ERR.RESPONSE", err.response);
          alert(err.response.status+ ''+ err.response.statusText);
        });
      },
      genTagcloud() {
        console.log("genTagcloud()..", this.tagwords);
        const cloud = require('d3-cloud');
        cloud()
          .words(this.tagwords)
          .padding(5)
          .font('Impact')
          .rotate(0)
          .text((d) => d.name)
          .fontSize(function(d) {return 10 + d.count * 10;})
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
            return 10 + d.count * 10 + "px";
          })
          .style('font-family', 'Impact')
          .style('opacity', 0.8)
          .attr('text-anchor', 'middle')
          .attr('transform', (d) => {
            return 'translate(' + [d.x, d.y] + ')rotate(' + d.rotate + ')';
          })
          .text((d) => d.name)        
          .on("click", function() {
              const tagname11 = d3.select(this).text();
              serverPagewithTag(tagname11);
            })
          function serverPagewithTag(tagname) {
            console.log("serverPagewithTag()...", tagname);
            location.href = `/blog/post/list/?tagname=${tagname}`;
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