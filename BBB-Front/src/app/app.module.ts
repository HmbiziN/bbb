import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { LandingComponent } from './Pages/landing/landing.component';
import { HeaderComponent } from './Components/header/header.component';
import { DashboardResultComponent } from './Components/Dashboard/dashboard-result/dashboard-result.component';
import { DashboardUpcomingComponent } from './Components/Dashboard/dashboard-upcoming/dashboard-upcoming.component';
import { NavComponent } from './Components/Utils/nav/nav.component';
import { FooterComponent } from './Components/Utils/footer/footer.component';
import { ActuComponent } from './Components/actu/actu.component';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { ClubPresComponent } from './Pages/club/club-pres/club-pres.component';
import { TechnicalTeamComponent } from './Components/club/technical-team/technical-team.component';
import { FunctionTeamComponent } from './Components/club/function-team/function-team.component';
import { TrainingComponent } from './Components/club/training/training.component';
import { SectionComponent } from './Components/section/section.component';
import { ContactPageComponent } from './Pages/contact-page/contact-page.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SliderComponent } from './Components/slider/slider.component';
import { CommonModule } from '@angular/common';
import { TestComponent } from './Components/partners/partners.component';
import { ErrorPageComponent } from './Components/Utils/error-page/error-page.component';
import { GaleryComponent } from './Components/galery/galery.component';
import { GaleryDetailComponent } from './Components/galery-detail/galery-detail.component';
import { InfosComponent } from './Components/infos/infos.component';
import { SpinnerComponent } from './Components/Utils/spinner/spinner.component';
import { TrainingFilterPipe } from './global/training-filter.pipe';
import { TimeFormatPipe } from './global/timeFormat.pipe';
import { NearestDatePipe } from './global/NearestDate.pipe';
import { CapitalizePipe } from './global/capitalize.pipe';
import { ExceptionalTrainingComponent } from './Components/club/exceptional-training/exceptional-training.component';
import { DayPipe } from './global/day.pipe';
import { DateFilterPipe } from './global/dateFilter.pipe';
import { HashLocationStrategy, LocationStrategy } from '@angular/common';

@NgModule({
  declarations: [
    AppComponent,
    LandingComponent,
    HeaderComponent,
    DashboardResultComponent,
    DashboardUpcomingComponent,
    NavComponent,
    FooterComponent,
    ActuComponent,
    ClubPresComponent,
    TechnicalTeamComponent,
    FunctionTeamComponent,
    TrainingComponent,
    SectionComponent,
    ContactPageComponent,
    SliderComponent,
    TestComponent,
    ErrorPageComponent,
    GaleryComponent,
    GaleryDetailComponent,
    InfosComponent,
    SpinnerComponent,
    TrainingFilterPipe,
    TimeFormatPipe,
    NearestDatePipe,
    CapitalizePipe,
    DayPipe,
    ExceptionalTrainingComponent,
    DateFilterPipe,
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [
    {provide: LocationStrategy, useClass: HashLocationStrategy}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
