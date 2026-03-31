# -*- coding: utf-8 -*-
from pathlib import Path

src = Path(r"D:\1c\MRS_HRS\DataProcessors\УстановкаДатЗапрета\Forms\Форма\Ext\Form.xml")
lines = src.read_text(encoding="utf-8").splitlines(keepends=True)

header = "".join(lines[0:35])

child_html = (
    "\t<ChildItems>\n"
    '\t\t<HTMLDocumentField name="ПолеHTMLДокумента" id="9000">\n'
    "\t\t\t<DataPath>ТекстПоляHTML</DataPath>\n"
    "\t\t\t<TitleLocation>None</TitleLocation>\n"
    "\t\t\t<Width>100</Width>\n"
    "\t\t\t<Height>30</Height>\n"
    "\t\t\t<HorizontalStretch>true</HorizontalStretch>\n"
    "\t\t\t<VerticalStretch>true</VerticalStretch>\n"
    '\t\t\t<ContextMenu name="ПолеHTMLДокументаКонтекстноеМеню" id="9001"/>\n'
    '\t\t\t<ExtendedTooltip name="ПолеHTMLДокументаРасширеннаяПодсказка" id="9002"/>\n'
    "\t\t\t<Events>\n"
    '\t\t\t\t<Event name="OnClick">ПолеHTMLДокументаПриНажатии</Event>\n'
    "\t\t\t</Events>\n"
    "\t\t</HTMLDocumentField>\n"
    "\t</ChildItems>\n"
)

attrs_block = "".join(lines[823:1533]).rstrip()
insert_attr = (
    "\n\t\t<Attribute name=\"ТекстПоляHTML\" id=\"20\">\n"
    "\t\t\t<Title>\n"
    "\t\t\t\t<v8:item>\n"
    "\t\t\t\t\t<v8:lang>ru</v8:lang>\n"
    "\t\t\t\t\t<v8:content>Текст поля HTML</v8:content>\n"
    "\t\t\t\t</v8:item>\n"
    "\t\t\t</Title>\n"
    "\t\t\t<Type>\n"
    "\t\t\t\t<v8:Type>xs:string</v8:Type>\n"
    "\t\t\t\t<v8:StringQualifiers>\n"
    "\t\t\t\t\t<v8:Length>0</v8:Length>\n"
    "\t\t\t\t\t<v8:AllowedLength>Variable</v8:AllowedLength>\n"
    "\t\t\t\t</v8:StringQualifiers>\n"
    "\t\t\t</Type>\n"
    "\t\t</Attribute>\n"
    "\t</Attributes>\n"
)
attrs = attrs_block + insert_attr

cmds = "".join(lines[1534:1651])
body = header + child_html + attrs + cmds + "</Form>\n"

out = Path(r"D:\1c\MRS_HRS\DataProcessors\УстановкаДатЗапрета\Forms\Форма_HTML\Ext\Form.xml")
out.write_text(body, encoding="utf-8")
print("OK", out, "bytes", len(body.encode("utf-8")))
