# coding=gbk


# import everything
import os
import getData
from flask import Flask
from flask import render_template
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid
from pyecharts.charts import Geo
from pyecharts.charts import Pie
from pyecharts.charts import WordCloud
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Scatter
from pyecharts.charts import Funnel
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType
import json


# Get CouchDB data
os.system("python getData.py")


# Flask routing
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

# round data to be two decimal places
def roundlist(old_list):
    newList = []
    for k in range(0, len(old_list)):
        for item in old_list:
            newitem = round(item, 2)
            newList.append(newitem)
    return newList


######################################## Scatter ##########################################################
co_friend_count = getData.covid_fc
j = 0
for i in range(len(co_friend_count)):
    if co_friend_count[j] > 20000:
        co_friend_count.pop(j)
    else:
        j += 1

cr_friend_count = getData.crime_fc

k = 0
for i in range(len(cr_friend_count)):
    if cr_friend_count[k] > 20000:
        cr_friend_count.pop(k)
    else:
        k += 1

covid_polarity = roundlist(getData.covid_p)
crime_polarity = roundlist(getData.crime_p)


def show_scatter():
    scatter = (
        Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
            .add_xaxis(xaxis_data=co_friend_count)
            .add_yaxis(
            series_name="Covid",
            y_axis=covid_polarity,
            symbol="triangle",
            symbol_size=15,
            label_opts=opts.LabelOpts(is_show=False),

        )
            .add_xaxis(xaxis_data=cr_friend_count)
            .add_yaxis(
            series_name="Crime",
            y_axis=crime_polarity,
            symbol="circle",
            symbol_size=15,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .set_series_opts()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Twitter Friend Count VS Polarity"),
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
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=1, min_=-1, range_text=['Positive', 'Negative'], ),
        ))
    return scatter


@app.route("/scatter")
def get_scatter():
    scatter = show_scatter()
    return scatter.dump_options_with_quotes()


@app.route("/friendcount")
def finals():
    return render_template("finalscatter.html")


################################ Pie #################################################################
co_positive_lan_type = getData.finalcopl
co_positive_lan_value = roundlist(getData.finalcopv)
co_negative_lan_type = getData.finalconl
co_negative_lan_value = roundlist(getData.finalconv)
cr_positive_lan_type = getData.finalcrpl
cr_positive_lan_value = roundlist(getData.finalcrpv)
cr_negative_lan_type = getData.finalcrnl
cr_negative_lan_value = roundlist(getData.finalcrnv)


def show_pie():
    pie = (
        Pie()
            .add(
            "",
            [list(z) for z in zip(co_positive_lan_type, co_positive_lan_value)],
            center=["20%", "30%"],
            radius=[60, 80],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),

        )
            .add(
            "",
            [list(z) for z in zip(co_negative_lan_type, co_negative_lan_value)],
            center=["55%", "30%"],
            radius=[60, 80],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),

        )
            .add(
            "",
            [list(z) for z in zip(cr_positive_lan_type, cr_positive_lan_value)],
            center=["20%", "70%"],
            radius=[60, 80],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),

        )
            .add(
            "",
            [list(z) for z in zip(cr_negative_lan_type, cr_negative_lan_value)],
            center=["55%", "70%"],
            radius=[60, 80],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),

        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="                                    Proportion of Different Languages"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )

    )
    return pie


@app.route("/pie")
def get_pie_chart():
    pie = show_pie()
    return pie.dump_options_with_quotes()


@app.route("/language")
def pie():
    return render_template("finalpie.html")


################################ Wordcloud ##########################################################
cowc = getData.cowordcount


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


@app.route("/wordcloud")
def finalcloud():
    return render_template("finalcloud.html")


crwc = getData.crwordcount


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


########################################## Bar ###############################################################
bar_city = getData.city_name
bar_income = getData.incomekk
bar_employ = getData.employkk

bar_co_p = roundlist(getData.arrange1)
bar_co_n = roundlist(getData.arrange2)
bar_cr_p = roundlist(getData.arrange3)
bar_cr_n = roundlist(getData.arrange4)


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
            .set_global_opts(title_opts=opts.TitleOpts(title="City Income"),
                             yaxis_opts=opts.AxisOpts(name="Income(k)/Employ(10k)/PosVSNeg"),
                             xaxis_opts=opts.AxisOpts(name="City"),
                             datazoom_opts=opts.DataZoomOpts(
                                 orient="horizontal",
                                 range_start=0,
                                 range_end=100
                             ),
                             toolbox_opts=opts.ToolboxOpts(), )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average", name="Average Value"),
                ]
            ),
        ))
    return bar


@app.route("/bar")
def get_bar():
    bar = show_bar()
    return bar.dump_options_with_quotes()


@app.route("/income")
def finalb():
    return render_template("finalbar.html")


###################################### Crime map ########################################################

geo_city = getData.city_name
geo_crv = getData.city_cr_allc
aurin_crcity = getData.aurincrcity
aurin_crv = getData.aurincr


def show_crime1():
    crime1 = (
        Geo()
            .add_schema(maptype="澳大利亚")
            .add_coordinate("Sydney", 151.207, -33.868)
            .add_coordinate("Melbourne", 144.963, -37.814)
            .add_coordinate("Brisbane", 153.028, -27.468)
            .add_coordinate("Perth", 115.861, -31.952)
            .add_coordinate("Adelaide", 138.599, -34.929)
            .add_coordinate("Cold Coast", 153.431, -28)
            .add_coordinate("Newcastle", 151.78, -32.93)
            .add("geo", [list(z) for z in zip(geo_city, geo_crv)], type_=ChartType.HEATMAP)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=500, min_=0,
                                              range_text=['Highly discussed', 'Rarely discussed']),
            title_opts=opts.TitleOpts(title="Twitter Crime Heatmap"),
            legend_opts=opts.LegendOpts(is_show=False),
        ))
    return crime1


@app.route("/crmap1")
def get_crime1():
    crmap1 = show_crime1()
    return crmap1.dump_options_with_quotes()


def show_crime2():
    crime2 = (
        Geo()
            .add_schema(maptype="澳大利亚")
            .add_coordinate("Sydney", 151.207, -33.868)
            .add_coordinate("Melbourne", 144.963, -37.814)
            .add_coordinate("Brisbane", 153.028, -27.468)
            .add_coordinate("Perth", 115.861, -31.952)
            .add_coordinate("Adelaide", 138.599, -34.929)
            .add("geo", [list(z) for z in zip(aurin_crcity, aurin_crv)], type_=ChartType.HEATMAP)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="color", max_=500, min_=0,
                                              range_text=['Frequently occurred', 'Rarely occurred']),
            title_opts=opts.TitleOpts(title="AURIN Crime Heatmap"),
            legend_opts=opts.LegendOpts(is_show=False)

        ))
    return crime2


@app.route("/crmap2")
def get_crime2():
    crmap2 = show_crime2()
    return crmap2.dump_options_with_quotes()


####################################### Covid map #########################################################

geo_cov = getData.city_co_allc


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
            .add("geo", [list(z) for z in zip(geo_city, geo_cov)])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=500, min_=0,
                                              range_text=['Highly discussed', 'Rarely discussed']),
            title_opts=opts.TitleOpts(title="Twitter Covid Map"),
            legend_opts=opts.LegendOpts(is_show=False)
        )
    )

    return covid


@app.route("/comap")
def get_covid():
    comap = show_covid()
    return comap.dump_options_with_quotes()

@app.route("/crime&covidmap")
def finalcrime():
    return render_template("map.html")




####################################### Funnel & bar #########################################################
f_x_data = getData.city_name
f_y1_data = getData.mental
fdata1 = [[f_x_data[i], f_y1_data[i]] for i in range(len(f_x_data))]


def show_funnel1():
    funnel1 = (
        Funnel(init_opts=opts.InitOpts(width="160px", height="80px"))
            .add(
            series_name="",
            data_pair=fdata1,
            gap=2,
            label_opts=opts.LabelOpts(is_show=True, position="inside"),
            itemstyle_opts=opts.ItemStyleOpts(border_color="#fff", border_width=1),
        )

            .set_global_opts(title_opts=opts.TitleOpts(title="City Mental Health Funnel"),
                             legend_opts=opts.LegendOpts(
                                 type_="scroll", pos_bottom="20%", pos_right="67%", orient="vertical"
                             )))
    return funnel1


@app.route("/funnel1")
def get_funnel1():
    funnel1 = show_funnel1()
    return funnel1.dump_options_with_quotes()


def show_bar2():
    bar2 = (
        Bar()
            .add_xaxis(bar_city)
            .add_yaxis("Covid Neg", bar_co_n, stack="stack1")
            .add_yaxis("Crime Neg", bar_cr_n, stack="stack1")
            .set_global_opts(title_opts=opts.TitleOpts(title="City Depression"),
                             yaxis_opts=opts.AxisOpts(name="Neg"),
                             xaxis_opts=opts.AxisOpts(name="City", axislabel_opts=opts.LabelOpts(rotate=-15)),
                             datazoom_opts=opts.DataZoomOpts(
                                 orient="vertical",
                                 range_start=0,
                                 range_end=100
                             )
                             )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="Min Value"),
                    opts.MarkLineItem(type_="max", name="Max Value"),
                    opts.MarkLineItem(type_="average", name="Average Value"),
                ]
            ),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="Max Value"),
                    opts.MarkPointItem(type_="min", name="Min Value"),
                    opts.MarkPointItem(type_="average", name="Average Value"),
                ]

            ),
        ))
    return bar2


@app.route("/bar2")
def get_bar2():
    bar2 = show_bar2()
    return bar2.dump_options_with_quotes()


@app.route("/mentalhealth")
def finalf():
    return render_template("finalfunnel.html")


#####################################  RUN ##################################################
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000,debug=True)
