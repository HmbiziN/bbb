import {
  Component,
  OnInit
} from '@angular/core';
import {
  CLUB
} from 'src/app/bbb';
import {
  PartnersService
} from 'src/app/Services/partners.service';

@Component({
  selector: 'app-partners',
  templateUrl: './partners.component.html',
  styleUrls: ['./partners.component.css']
})
export class TestComponent implements OnInit {
  public partners: CLUB.Partners[];
  constructor(private partnersService: PartnersService) {}

  ngOnInit(): void {
    this.getPartners()
  }
  public getPartners() {
    this.partnersService.getAllPartners()
      .subscribe({
        next: (r) => {
          this.partners = r
        }
      })
  }

  public openWebsite(url: string) {
    if (url != null) {
      window.open(url, "_blank")
    }
  }
}
