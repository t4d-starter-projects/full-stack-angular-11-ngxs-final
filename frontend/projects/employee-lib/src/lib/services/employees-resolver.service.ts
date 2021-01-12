import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { Employee } from '../models/Employee';
import { EmployeesService } from './employees.service';


@Injectable({
  providedIn: 'root'
})
export class EmployeesResolverService implements Resolve<Employee[]> {

  constructor(private employeesSvc: EmployeesService) { }

  resolve(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot):
    Employee[] | Observable<Employee[]> | Promise<Employee[]> {
    return this.employeesSvc.all();
  }
}
