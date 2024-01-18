import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FunctionTeamComponent } from './function-team.component';

describe('FunctionTeamComponent', () => {
  let component: FunctionTeamComponent;
  let fixture: ComponentFixture<FunctionTeamComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FunctionTeamComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FunctionTeamComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
