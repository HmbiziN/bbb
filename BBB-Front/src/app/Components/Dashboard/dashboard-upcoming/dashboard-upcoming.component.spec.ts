import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardUpcomingComponent } from './dashboard-upcoming.component';

describe('DashboardUpcomingComponent', () => {
  let component: DashboardUpcomingComponent;
  let fixture: ComponentFixture<DashboardUpcomingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DashboardUpcomingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DashboardUpcomingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
