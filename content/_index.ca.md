---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        Laboratori de Remodelació Tisular, Fibrosi i Càncer
      image:
        filename: welcome2.jpg
      cta:
        label: 'Contacta'
        url: /contact/
      cta_alt:
        label: "Coneix l'equip"
        url: /people/
      text: |
        <br>
        Liderat per la Doctora Anna Moles, el grup de Remodelació Tisular, Fibrosi i Càncer té un enfocament científic transversal, amb un equip punter d'investigadors que treballa amb les técniques més avançades.
        <br/>

  - block: collection
    content:
      title: Línies de recerca
      text:
      count: 4
      offset: 0
      order: desc
      page_type: lines
    design:
      view: showcase2
      columns: '1'

  - block: collection
    content:
      title: Notícies
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      columns: '1'

---
