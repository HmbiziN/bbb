import {
  Component,
  OnInit
} from '@angular/core';
import {
  CLUB
} from 'src/app/bbb';
import {
  ActuService
} from 'src/app/Services/actu.service';

@Component({
  selector: 'app-actu',
  templateUrl: './actu.component.html',
  styleUrls: ['./actu.component.css']
})
export class ActuComponent implements OnInit {
  public actu: CLUB.Actu[];
  public currentDate: Date; 
  constructor(
    private actuService: ActuService
  ) {}

  ngOnInit(): void {
    this.getActu();
  }

  public getActu() {
    this.actuService.getActu()
      .subscribe({
        next: (r: CLUB.Actu[]) => {
          this.actu = r
        }
      })
  }

}
