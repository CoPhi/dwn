tree=ET.parse("retag.xml")
root = tree.getroot()
generale={}
for synset in root.iter('synset'):
	ide=synset.get('id')
	che=synset.get('checked')
	greco=synset.find('grc')
	if greco is not None:
		for w in greco.iter('w'):
                    meta=[]
                    senso=[]
                    if che is not None:
                        meta.append("YB")
                        meta.append(che)
		    key=w.text+'_'+ide[0]
		    con=w.get('in')
		    meta.append(con)
		    if key not in generale:
                        sen=w.text+'_'+str(1)+'_'+ide
                        senso.append(sen)
                        senso.append(meta)
                        generale[key]=[senso]
		    elif key in generale:
				tmp=generale.get(key)
				sen=w.text+'_'+str(len(tmp)+1)+' '+ide
				senso.append(sen)
				senso.append(meta)
				tmp.append(senso)



wordnet=ET.Element('wordnet')
for l in generale:
	lexent=ET.SubElement(wordnet,'LexicalEntry')
	le = l.split('_')
	lemma=ET.SubElement(lexent,"Lemma",attrib={"writtenForm":le[0], "partOfSpeech":le[1]})
	for s in generale.get(l):
		se = s[0].split('_')
		senso=ET.SubElement(lexent,"Sense",attrib={"id":se[0], "synset":se[1]})
		if len(s[1])<2:
			met=ET.SubElement(senso,"Meta",attrib={"confidenceScore":s[1][0]})
                if len(s[1])>2:
			met=ET.SubElement(senso,"Meta",attrib={"author":s[1][0], "date":s[1][1], "confidenceScore":s[1][2]})



