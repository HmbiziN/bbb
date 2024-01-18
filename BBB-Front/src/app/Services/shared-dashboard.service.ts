import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators'
import { DASHBOARD } from 'src/app/bbb';
import { ResultService } from 'src/app/Services/result.service';
import { UpcomingService } from 'src/app/Services/upcoming.service';

@Injectable({
  providedIn: 'root'
})
export class SharedDashboardService {
  public result: DASHBOARD.Upcoming[] = [];
  public dataNull: boolean = false;

  constructor(
    private resultService: ResultService,
    private upcomingService: UpcomingService
  ) { }

  public getResult(section: number = null) : Observable<DASHBOARD.Result[]> {
    return this.resultService.getResult().pipe(map((r:[])=>{
        let res = r as DASHBOARD.Result[];
        if (section !== null) {
            res = res.filter(result => result.section === section);
        }
        return res;
    }))
}

  public getMatch(section: number) : Observable<DASHBOARD.Upcoming[]> {
    return this.upcomingService.getUpcoming()
    .pipe(
        map((r:[]) => {
            let res = r as DASHBOARD.Upcoming[];
            if (section !== null) {
                res = res.filter(result => result.section === section);
            }
            return res;
        })
    )
  }

}
