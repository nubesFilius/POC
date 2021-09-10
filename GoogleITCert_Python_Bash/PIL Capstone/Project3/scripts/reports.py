#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
import locale, operator

def generate(filename, title, additional_info, table_data, data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)

  # Create a dictionary with Total Sales per Car Maker
  car_sales = {}
  for row in data:
      if row["car"]["car_make"] not in car_sales.keys():
          car_sales[row["car"]["car_make"]] = row["total_sales"]
      else:
          car_sales[row["car"]["car_make"]] += row["total_sales"]

  # Create a dictionary for Bar Chart with Revenue per Car Maker
  car_revenue = {}
  for row in data:
      item_price = locale.atof(row["price"].strip("$"))
      item_revenue = row["total_sales"] * item_price
      if row["car"]["car_make"] not in car_revenue.keys():
          car_revenue[row["car"]["car_make"]] = int(item_revenue)
      else:
          car_revenue[row["car"]["car_make"]] += int(item_revenue)
  top10 = sorted(car_revenue.items(), key=operator.itemgetter(1), reverse=True)[:10]

  # PIE CHART
  report_pie = Pie()
  report_pie.data = []
  report_pie.labels = []

  for car, sales in car_sales.items():
    report_pie.labels.append(car)
    report_pie.data.append(sales)

  report_chart = Drawing(400,200)
  report_pie.x = 25
  report_pie.y = -300
  report_pie.width = 400
  report_pie.height = 500
  report_pie.slices.strokeWidth=0.5
  report_chart.add(report_pie)

  # BUILD BAR CHART
  data = []
  axis = []
  for k, v in top10:
      data.append(v)
      axis.append(k)

  report_bar = Drawing(400, 200)
  bc = VerticalBarChart()
  bc.x = 0
  bc.y = -325
  bc.height = 125
  bc.width = 500
  bc.data = [tuple(data)]
  bc.strokeColor = colors.black
  bc.categoryAxis.categoryNames = axis
  report_bar.add(bc)

  # BUILD THE ENTIRE PDF REPORT
  report.build([report_title, empty_line, report_info, empty_line, report_table, report_chart, report_bar])
