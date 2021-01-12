import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatCardModule } from '@angular/material/card';

import { EmployeeLibModule } from '@t4d-wnow/employee-lib';
import { EmployeeToolRoutingModule } from './employee-tool.routing';
import { EmployeesComponent } from './pages/employees/employees.component';


@NgModule({
  declarations: [EmployeesComponent],
  imports: [
    CommonModule,
    FlexLayoutModule,
    MatCardModule,
    EmployeeLibModule,
    EmployeeToolRoutingModule,
  ]
})
export class EmployeeToolModule { }
