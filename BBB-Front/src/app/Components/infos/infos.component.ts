import {
  Component,
  OnInit
} from '@angular/core';
import * as L from 'leaflet'
import {
  CLUB
} from 'src/app/bbb';
import {
  ClubService
} from 'src/app/Services/club.service';

@Component({
  selector: 'app-infos',
  templateUrl: './infos.component.html',
  styleUrls: ['./infos.component.css']
})
export class InfosComponent implements OnInit {
  public map: any
  public coords: CLUB.Coordinates[] = [{
      name: "Halle des sports",
      adress: "",
      lat: 45.29638986814711,
      lng: 3.3906543690181374
    },
    {
      name: "Lycée Lafayette",
      adress: "Av. Cochet de Saint-Vallier, 43100 Brioude",
      lat: 45.295564,
      lng: 3.386482
    },
    {
      name: "Salle polyvalente & Gymnase",
      adress: "Rue de la Croix Saint-Isidore, 43100 Brioude",
      lat: 45.29808363379214,
      lng: 3.390451961376416
    },
  ]


  public markerbbb = L.icon({
    iconUrl: 'assets/icons8.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [0, -41]
  })
  public licences: CLUB.Licence[]

  constructor(private clubService: ClubService) {}

  ngOnInit(): void {
    const centre: {
      lat: number,
      lng: number
    } = {
      lat: 45.295564,
      lng: 3.386482
    }
    this.map = L.map('map').setView(centre, 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'données OpenSreetMap France',
      minZoom: 1,
      maxZoom: 20
    }).addTo(this.map)
    this.addMarker(this.coords)
    this.getLicence()
  }

  public addMarker(coords: CLUB.Coordinates[]) {
    for (const c of coords) {
      const marker = L.marker([c.lat, c.lng], {
          icon: this.markerbbb
        })
        .addTo(this.map)
      marker.bindPopup((`<br>${c.name}</br>${c.adress}<br/>`))
    }
  }

  public getLicence() {
    this.clubService.getLicence()
      .subscribe({
        next: (r: CLUB.Licence[]) => {
          this.licences = r;
        }
      })
  }
}
