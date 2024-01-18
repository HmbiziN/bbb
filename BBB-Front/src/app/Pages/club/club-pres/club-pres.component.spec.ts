import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClubPresComponent } from './club-pres.component';

describe('ClubPresComponent', () => {
  let component: ClubPresComponent;
  let fixture: ComponentFixture<ClubPresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClubPresComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClubPresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
