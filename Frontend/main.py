import os

from flask import Flask
from flask import render_template
# docs_by_author = ViewDefinition('docs', 'byauthor',
#                                 'function(doc) { emit(doc.author, doc);}')
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid
from pyecharts.charts import Gauge
from pyecharts.charts import Geo
from pyecharts.charts import Pie
from pyecharts.charts import Radar
from pyecharts.charts import WordCloud
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Scatter
import getData
from pyecharts.charts import Funnel
from pyecharts.charts import Grid
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import json


os.system("python getData.py")
# user = "admin"
# password = "password"
# couchserver = couchdb.Server("http://%s:%s@172.26.132.125:5555/" % (user, password))
#
# # for dbname in couchserver:
# # print(dbname)
#
# dbname = "cov_friends_vs_polarity"
# if dbname in couchserver:
#     db = couchserver[dbname]
# else:
#     db = couchserver.create(dbname)
#
# # doc_id = "created:dedup_twitter"
# # doc = db[doc_id]
# # print(doc)
#
#
# for item in db.view('_design/newdoc/_view/new-view', include_docs=True):
#     temp = item.doc
#     print(dir(temp))
#     print(type(temp))
#     print(temp['Ballarat'])
# data = temp.__dict__
# print(jsonify(data))
# curl http://admin:password@172.26.132.232:5984/_global_changes/_all_docs
# curl "http://admin:password@172.26.132.232:5984/_global_changes/_all_docs?include_docs=true&key=\"created:dedup_twit
# ter\"


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/map")
def map():
    return render_template("map.html")


@app.route("/part2")
def part2():
    return render_template("part2.html")


@app.route("/part3")
def part3():
    return render_template("part3.html")


@app.route("/chart")
def chart():
    return render_template("pie.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/basic")
def basic():
    return render_template("basic.html")


# @app.route("/<author_id>/docs")
# def docs(author_id):
#     docs = []
#     for row in docs_by_author(g.couch)[author_id]:
#         docs.append(row.value)
#     return simplejson.dumps(docs)

# @app.route('/form_to_json', methods=['POST'])
# def form_to_json():
#     # data = request.form.to_dict(flat=False)
#     return jsonify(data)

######################################## Scatter ##########################################################
# friend_count = [666, 100, 3, 888, 1000, 200, 50]
# covid_polarity = [0.5, 0.1, -0.4, 0.7, 0.9, 0.3, -0.1]
# crime_polarity = [-0.5, 0.3, 0.9, -0.7, -0.75, 0.6, 0.8]

co_friend_count = getData.covid_fc
cr_friend_count = getData.crime_fc
covid_polarity = getData.covid_p
crime_polarity = getData.crime_p


def show_scatter():
    scatter = (
        Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
            .add_xaxis(xaxis_data=co_friend_count)
            # .add_yaxis("Covid", )
            .add_yaxis(
            series_name="Covid",
            y_axis=covid_polarity,
            symbol="triangle",
            symbol_size=25,
            label_opts=opts.LabelOpts(is_show=False),

        )
            .add_xaxis(xaxis_data=cr_friend_count)
            .add_yaxis(
            series_name="Crime",
            y_axis=crime_polarity,
            symbol="circle",
            symbol_size=25,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_series_opts()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Scatter-VisualMap(Size)"),
            xaxis_opts=opts.AxisOpts(
                name='Friend Count',
                name_location='middle',
                name_gap=20,
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            yaxis_opts=opts.AxisOpts(
                name='Polarity',
                name_location='middle',
                name_gap=20,
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            # tooltip_opts=opts.TooltipOpts(is_show=False),
            toolbox_opts=opts.ToolboxOpts(),
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=1, min_=-1, range_text=['Positive', 'Negative'],),
        ))
    return scatter


@app.route("/scatter")
def get_scatter():
    scatter = show_scatter()
    return scatter.dump_options_with_quotes()


@app.route("/finals")
def finals():
    return render_template("finas.html")


########################### Gauge ##########################################
def show_gauge():
    gauge = (
        Gauge()
            .add(
            "Total Condition",
            [("Depression Rate            ", 60.8)],
            split_number=5,
            radius="50%",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total Condition about Australia Depression Rate"),
            legend_opts=opts.LegendOpts(is_show=False),
        ))
    return gauge


@app.route("/gague")
def get_gague():
    gague = show_gauge()
    return gague.dump_options_with_quotes()


@app.route("/finalg")
def finalg():
    return render_template("finalgague.html")


######################################## Radar ##########################################################
radar1 = [[4300, 10000, 28000, 35000]]
radar2 = [[5000, 14000, 28000, 31000]]


def show_radar():
    radar = (
        Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="#CCCCCC"))
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="Friend Count", max_=6500),
                opts.RadarIndicatorItem(name="Income", max_=16000),
                opts.RadarIndicatorItem(name="Language", max_=30000),
                opts.RadarIndicatorItem(name="Mental Health", max_=38000),
                # opts.RadarIndicatorItem(name="Development", max_=52000),
                # opts.RadarIndicatorItem(name="Marketing", max_=25000),
            ],
            splitarea_opt=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            textstyle_opts=opts.TextStyleOpts(color="#fff"),
        )
            .add(
            series_name="Covid",
            data=radar1,
            linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
        )
            .add(
            series_name="Crime",
            data=radar2,
            linestyle_opts=opts.LineStyleOpts(color="#5CACEE"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Covid VS Crime"), legend_opts=opts.LegendOpts()
        ))
    return radar


@app.route("/radar")
def get_radar():
    radar = show_radar()
    return radar.dump_options_with_quotes()


@app.route("/finalr")
def finalr():
    return render_template("finalradar.html")


################################ Pie #####################################
co_positive_lan_type=getData.finalcopl
co_positive_lan_value=getData.finalcopv
co_negative_lan_type=getData.finalconl
co_negative_lan_value=getData.finalconv
cr_positive_lan_type=getData.finalcrpl
cr_positive_lan_value=getData.finalcrpv
cr_negative_lan_type=getData.finalcrnl
cr_negative_lan_value=getData.finalcrnv

#print(co_negative_lan_type)
def show_pie():
    # fn = """
    #     function(params) {
    #         if(params.name == '其他')
    #             return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
    #         return params.name + ' : ' + params.value + '%';
    #     }
    #     """
    #
    # def new_label_opts():
    #     return opts.LabelOpts(formatter=JsCode(fn), position="center")

    pie = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(co_positive_lan_type,co_positive_lan_value)],
            center=["20%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(co_negative_lan_type, co_negative_lan_value)],
            center=["55%", "30%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(cr_positive_lan_type, cr_positive_lan_value)],
            center=["20%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .add(
            "",
            [list(z) for z in zip(cr_negative_lan_type,cr_negative_lan_value )],
            center=["55%", "70%"],
            radius=[60, 80],
            # label_opts=new_label_opts(),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Mult Pie"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
            ),
        )

    )
    return pie
    # pie = (
    #     Pie()
    #         .add("", [("Melbourne", 100), ("Sydney", 1000), ("Perth", 2000)])
    #         .set_global_opts(title_opts=opts.TitleOpts(title="Pie"))
    #         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #
    # )
    #
    # return render_template('show_charts.html',
    #                        bar_options=bar.dump_options(),
    #                        pie_options=pie.dump_options())


@app.route("/pie")
def get_pie_chart():
    pie = show_pie()
    return pie.dump_options_with_quotes()


@app.route("/finalp")
def pie():
    return render_template("finalp.html")


################################ Wordcloud ###############################################
cowc=getData.cowordcount

def show_cloud():
    cloud = (
        WordCloud()
            .add("", cowc, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
    )
    return cloud

@app.route("/cloud")
def get_cloud():
    cloud = show_cloud()
    return cloud.dump_options_with_quotes()


@app.route("/finalcloud")
def finalcloud():
    return render_template("finalcloud.html")

################################ Wordcloud ###############################################
crwc=getData.crwordcount

def show_cloud2():
    cloud2 = (
        WordCloud()
            .add("", crwc, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
    )
    return cloud2

@app.route("/cloud2")
def get_cloud2():
    cloud2 = show_cloud2()
    return cloud2.dump_options_with_quotes()


@app.route("/finalcloud2")
def finalcloud2():
    return render_template("finalcloud2.html")

################################# Bar #####################################
bar_value_one = [50, 20, 30, 80, 60, 10]
bar_value_two = [100, 15, 60, 180, 40, 55]


# @app.route('/echart')
def show_charts():
    bar = (
        Bar()
            .add_xaxis(["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Canberra"])
            .add_yaxis("2017", bar_value_one)
            .add_yaxis("2021", bar_value_two)

            .set_global_opts(title_opts=opts.TitleOpts(title="Compare Bar"),
                             yaxis_opts=opts.AxisOpts(name="Y"),
                             xaxis_opts=opts.AxisOpts(name="X"),
                             toolbox_opts=opts.ToolboxOpts(), )
            # .set_global_opts(title_opts=opts.TitleOpts(title="Bar", subtitle="AB compare"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="Max Value"),
                    opts.MarkPointItem(type_="min", name="Min Value"),
                    opts.MarkPointItem(type_="average", name="Average Value"),
                ]

            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="Min Value"),
                    opts.MarkLineItem(type_="max", name="Max Value"),
                    opts.MarkLineItem(type_="average", name="Average Value"),
                ]
            ),
        ))
    return bar


@app.route("/echart")
def get_bar_chart():
    bar = show_charts()
    return bar.dump_options_with_quotes()


@app.route("/part1")
def part1():
    return render_template("part1.html")


#########################################################################################################
bar_city=getData.city_name
bar_income=getData.income
bar_employ=getData.employ

bar_co_p = getData.arrange1
bar_co_n = getData.arrange2
bar_cr_p = getData.arrange3
bar_cr_n = getData.arrange4



def show_bar():
    bar = (
        Bar()
            .add_xaxis(bar_city)
            .add_yaxis("Average Income", bar_income)
            .add_yaxis("Employed People", bar_employ)
            .add_yaxis("Covid Pos", bar_co_p, stack="stack1")
            .add_yaxis("Covid Neg", bar_co_n, stack="stack1")
            .add_yaxis("Crime Pos", bar_cr_p, stack="stack2")
            .add_yaxis("Crime Neg", bar_cr_n, stack="stack2")
            .set_global_opts(title_opts=opts.TitleOpts(title="Compare Bar"),
                             yaxis_opts=opts.AxisOpts(name="Income/Employment/Pos VS Neg"),
                             xaxis_opts=opts.AxisOpts(name="City"),
                             toolbox_opts=opts.ToolboxOpts(), )
            # .set_global_opts(title_opts=opts.TitleOpts(title="Bar", subtitle="AB compare"))
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="Max Value"),
                    opts.MarkPointItem(type_="min", name="Min Value"),
                    opts.MarkPointItem(type_="average", name="Average Value"),
                ]

            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="Min Value"),
                    opts.MarkLineItem(type_="max", name="Max Value"),
                    opts.MarkLineItem(type_="average", name="Average Value"),
                ]
            ),
        ))
    return bar


@app.route("/bar")
def get_bar():
    bar = show_bar()
    return bar.dump_options_with_quotes()


@app.route("/finalb")
def finalb():
    return render_template("finalb.html")


###################################### Crime map ########################################################
#city = ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Newcastle']
# covid_values = [10, 20, 30, 100, 50, 60, 70, 80, 90, 0]
#crime_values = [10, 20, 30, 100, 50, 60, 70]

geo_city = getData.city_name
geo_crv = getData.city_cr_allc


def show_crime():
    crime = (
        Geo()
            .add_schema(maptype="澳大利亚")
            .add_coordinate("Sydney", 151.207, -33.868)
            .add_coordinate("Melbourne", 144.963, -37.814)
            .add_coordinate("Brisbane", 153.028, -27.468)
            .add_coordinate("Perth", 115.861, -31.952)
            .add_coordinate("Adelaide", 138.599, -34.929)
            .add_coordinate("Cold Coast", 153.431, -28)
            .add_coordinate("Newcastle", 151.78, -32.93)
            .add("geo", [list(z) for z in zip(geo_city, geo_crv)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=10, min_=0), title_opts=opts.TitleOpts(title="Map")
        ))
    return crime


@app.route("/crmap")
def get_crime():
    crmap = show_crime()
    return crmap.dump_options_with_quotes()


@app.route("/finalcrime")
def finalcrime():
    return render_template("crimemap.html")




####################################### Covid #########################################################

geo_cov = getData.city_co_allc
# @app.route('/covidmap')
def show_covid():
    covid = (
        Geo()
            .add_schema(maptype="澳大利亚")
            .add_coordinate("Sydney", 151.207, -33.868)
            .add_coordinate("Melbourne", 144.963, -37.814)
            .add_coordinate("Brisbane", 153.028, -27.468)
            .add_coordinate("Perth", 115.861, -31.952)
            .add_coordinate("Adelaide", 138.599, -34.929)
            .add_coordinate("Cold Coast", 153.431, -28)
            .add_coordinate("Newcastle", 151.78, -32.93)
            .add("geo", [list(z) for z in zip(geo_city, geo_cov)], type_=ChartType.HEATMAP)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=10, min_=0), title_opts=opts.TitleOpts(title="Map")
        )
    )

    return covid


@app.route("/comap")
def get_covid():
    comap = show_covid()
    return comap.dump_options_with_quotes()


@app.route("/finalcovid")
def finalcovid():
    return render_template("covidmap.html")



####################################### Funnel #########################################################
f_x_data = getData.city_name
f_y1_data = getData.mental
f_y2_data = getData.arrange2
f_y3_data = getData.arrange4

fdata1 = [[f_x_data[i], f_y1_data[i]] for i in range(len(f_x_data))]
fdata2 = [[f_x_data[i], f_y2_data[i]] for i in range(len(f_x_data))]
fdata3 = [[f_x_data[i], f_y3_data[i]] for i in range(len(f_x_data))]

# funnel1 = (
#             Funnel(init_opts=opts.InitOpts(width="1600px", height="800px"))
#                 .add(
#                 series_name="",
#                 data_pair=fdata1,
#                 gap=2,
#                 # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
#                 label_opts=opts.LabelOpts(is_show=True, position="inside"),
#                 itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
#             )
#                 .set_global_opts(title_opts=opts.TitleOpts(title="Funnel")
#         ))



def show_funnel():
    funnel1 = (
        Funnel(init_opts=opts.InitOpts(width="160px", height="80px"))
            .add(
            series_name="",
            data_pair=fdata1,
            gap=2,
            # tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}%"),
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Funnel")
                             ))
    # funnel2 = (
    #     Funnel()
    #         .add(
    #         series_name="",
    #         data_pair=fdata2,
    #         gap=2,
    #         label_opts=opts.LabelOpts(is_show=True, position="inside"),
    #         itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
    #     )
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(title="Grid-Line", pos_right="5%"),
    #         legend_opts=opts.LegendOpts(pos_right="20%"),
    #     ))
    # fgrid = (
    #     Grid()
    #         .add(funnel1, grid_opts=opts.GridOpts(pos_bottom="60%"))
    #         .add(funnel2, grid_opts=opts.GridOpts(pos_top="60%"))

    return funnel1


@app.route("/funnel")
def get_funnel():
    funnel = show_funnel()
    return funnel.dump_options_with_quotes()


@app.route("/finalf")
def finalf():
    return render_template("finalf.html")






#######################################################################################
if __name__ == "__main__":
    app.run(debug=True)

    # app.config.update(
    #     DEBUG=True,
    #     COUCHDB_SERVER='http://admin:password@172.26.132.232:5984/',
    #     COUCHDB_DATABASE='_global_changes'
    # )
    # manager = flaskext.couchdb.CouchDBManager()
    # manager.setup(app)
    # manager.add_viewdef(docs_by_author)  # Install the view
    # manager.sync(app)
    # #app.run(host='0.0.0.0', port=5000)

# @app.route('/crimemap')
# def show_crimemap():
#     # crime = (
#     #     Geo()
#     #         .add_schema(maptype="澳大利亚")
#     #         .add_coordinate("Sydney", 151.207, -33.868)
#     #         .add_coordinate("Melbourne", 144.963, -37.814)
#     #         .add_coordinate("Brisbane", 153.028, -27.468)
#     #         .add_coordinate("Perth", 115.861, -31.952)
#     #         .add_coordinate("Adelaide", 138.599, -34.929)
#     #         .add_coordinate("Cold Coast", 153.431, -28)
#     #         .add_coordinate("Canberra", 149.128, -35.283)
#     #         .add_coordinate("Newcastle", 151.78, -32.93)
#     #         .add_coordinate("Hobart", 147.329, -42.879)
#     #         .add_coordinate("Darwin", 130.844, -12.464)
#     #         .add("geo", [list(z) for z in zip(city, crime_values)])
#     #         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     #         .set_global_opts(
#     #         visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="Map")
#     #     )
#     #         .render("templates/crimes_map!.html")
#     # )
#
#     return render_template("crime_map.html")
