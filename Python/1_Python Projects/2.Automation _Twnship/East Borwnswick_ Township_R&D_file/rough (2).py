from pyquery import PyQuery

html = """<table cellspacing="0" class="fk-specs-type2">
        <tr>
            <th class="group-head" colspan="2">Book Details</th>
        </tr>
                                                                                    <tr>
                <td class="specs-key">Publisher</td>
                <td class="specs-value fk-data">HARPER COLLINS INDIA</td>
            </tr>
                                                                                    <tr>
                <td class="specs-key">ISBN-13</td>
                <td class="specs-value fk-data">9789350291924</td>
            </tr>

                </table>
"""

doc = PyQuery(html)

for td in doc("table.fk-specs-type2").find("td.specs-key"):
    print td.text, td.getnext().text